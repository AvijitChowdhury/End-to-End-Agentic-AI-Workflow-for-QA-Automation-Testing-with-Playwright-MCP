FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME=/opt/poetry

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    ca-certificates \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    libdbus-1-3 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip setuptools
RUN python -m pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root

COPY . /app
RUN python -m playwright install --with-deps

ENTRYPOINT ["poetry", "run"]
CMD ["pytest", "-q", "--workers", "auto", "--dist", "loadfile"]
