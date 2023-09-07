FROM python:3.10

RUN pip install poetry==1.6.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /usr/src/app

# COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt 

COPY pyproject.toml poetry.lock README.md ./

COPY scripts/uuid_extension.sql /docker-entrypoint-initdb.d

RUN poetry install --no-root

COPY . .

RUN poetry install --no-root

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]