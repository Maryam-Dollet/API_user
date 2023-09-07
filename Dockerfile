FROM python:3.10

WORKDIR /usr/src/app

RUN pip install poetry

COPY pyproject.toml poetry.lock README.md ./

RUN poetry install

COPY . .


CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]