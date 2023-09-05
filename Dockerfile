FROM python:3.10-slim-bookworm

RUN pip install poetry

COPY app /api/
COPY pyproject.toml poetry.lock README.md /api/

WORKDIR /api

RUN poetry install

CMD ["poetry", "run", "uvicorn", "app.main:app"]