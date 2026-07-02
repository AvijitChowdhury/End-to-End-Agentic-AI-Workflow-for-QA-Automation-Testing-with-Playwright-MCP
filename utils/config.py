import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def _required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise EnvironmentError(f'Missing required environment variable: {name}')
    return value

ENV = os.environ.get('TEST_ENV', 'staging')
BASE_URL = _required_env('BASE_URL')
USERNAME = _required_env('SAUCEDEMO_USER')
PASSWORD = _required_env('SAUCEDEMO_PASSWORD')

REPORT_DIR = BASE_DIR / 'reports'
LOG_DIR = BASE_DIR / 'logs'
TEST_RESULTS_DIR = BASE_DIR / 'test-results'
SCREENSHOT_DIR = TEST_RESULTS_DIR / 'screenshots'
TRACE_DIR = TEST_RESULTS_DIR / 'traces'
VIDEO_DIR = TEST_RESULTS_DIR / 'videos'

REPORT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
TRACE_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)
