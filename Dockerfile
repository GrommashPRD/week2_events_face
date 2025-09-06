FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim AS base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

FROM base AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --all-groups

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --all-groups

FROM base

COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
