import logging
import os
import shutil
from pathlib import Path

import pytest

try:
    import allure
except ImportError:
    allure = None

from utils.config import BASE_URL, LOG_DIR, REPORT_DIR, SCREENSHOT_DIR, TRACE_DIR, VIDEO_DIR

WORKER_ID = 'master'
LOGGER = logging.getLogger('qa')


def get_worker_id(config) -> str:
    if hasattr(config, 'workerinput'):
        return config.workerinput.get('workerid', 'master')
    return os.environ.get('PYTEST_XDIST_WORKER', 'master')


def configure_logging(config) -> None:
    log_dir = Path(LOG_DIR)
    log_dir.mkdir(parents=True, exist_ok=True)
    worker = get_worker_id(config)
    log_path = log_dir / f'test-{worker}.log'

    handlers = [logging.StreamHandler(), logging.FileHandler(log_path, encoding='utf-8')]
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=handlers,
        force=True,
    )
    logging.getLogger('asyncio').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    LOGGER.info('Configured logging for worker: %s', worker)


def pytest_configure(config):
    global WORKER_ID
    WORKER_ID = get_worker_id(config)
    configure_logging(config)


@pytest.fixture(scope='session')
def logger() -> logging.Logger:
    return LOGGER


@pytest.fixture(scope='session')
def env() -> str:
    from utils.config import ENV

    return ENV


@pytest.fixture(scope='session')
def base_url() -> str:
    from utils.config import BASE_URL

    return BASE_URL


@pytest.fixture(scope='session')
def video_dir() -> str:
    video_dir = Path(VIDEO_DIR) / WORKER_ID
    video_dir.mkdir(parents=True, exist_ok=True)
    return str(video_dir)


@pytest.fixture
def browser_context_args(video_dir):
    return {
        'record_video_dir': video_dir,
        'record_video_size': {'width': 1280, 'height': 720},
    }


def pytest_runtest_logstart(nodeid, location):
    LOGGER.info('Starting test: %s', nodeid)


def pytest_runtest_logreport(report):
    if report.when != 'call':
        return

    if report.passed:
        LOGGER.info('Test passed: %s', report.nodeid)
    elif report.skipped:
        LOGGER.warning('Test skipped: %s', report.nodeid)
    elif report.failed:
        LOGGER.error('Test failed: %s', report.nodeid)

    retry_count = getattr(report, 'rerun', 0)
    if retry_count:
        LOGGER.warning('Retry attempt %s for %s', retry_count, report.nodeid)


@pytest.fixture(autouse=True)
def trace_on_every_test(request):
    if 'page' not in request.fixturenames:
        yield
        return

    page = request.getfixturevalue('page')
    trace_dir = Path(TRACE_DIR) / WORKER_ID
    trace_dir.mkdir(parents=True, exist_ok=True)
    trace_path = trace_dir / f'{request.node.name}.zip'

    context = getattr(page, 'context', None)
    if context is not None and hasattr(context, 'tracing'):
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    try:
        if context is not None and hasattr(context, 'tracing'):
            context.tracing.stop(path=str(trace_path))
            LOGGER.info('Saved Playwright trace to %s', trace_path)
    except Exception as exc:
        LOGGER.warning('Unable to save trace for %s: %s', request.node.name, exc)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        page = item.funcargs.get('page')
        if page is not None:
            screenshot_dir = Path(SCREENSHOT_DIR) / WORKER_ID
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshot_dir / f'{item.name}.png'
            try:
                page.screenshot(path=str(screenshot_path), full_page=True)
                LOGGER.info('Captured screenshot for failed test: %s', screenshot_path)
                if allure:
                    allure.attach.file(
                        str(screenshot_path),
                        name=f'{item.name} screenshot',
                        attachment_type=allure.attachment_type.PNG,
                    )
            except Exception as exc:
                LOGGER.warning('Failed to capture screenshot for %s: %s', item.name, exc)

            video_dir = Path(VIDEO_DIR) / WORKER_ID
            video_dir.mkdir(parents=True, exist_ok=True)
            try:
                video = getattr(page, 'video', None)
                if video is not None and hasattr(video, 'path'):
                    video_source = video.path()
                    if video_source and Path(video_source).exists():
                        video_dest = video_dir / f'{item.name}.webm'
                        shutil.copy(video_source, video_dest)
                        LOGGER.info('Saved video for failed test: %s', video_dest)
                        if allure:
                            allure.attach.file(
                                str(video_dest),
                                name=f'{item.name} video',
                                attachment_type=allure.attachment_type.WEBM,
                            )
            except Exception as exc:
                LOGGER.warning('Failed to save video for %s: %s', item.name, exc)
