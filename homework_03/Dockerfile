FROM python:3.9.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /user/app

RUN pip install poetry==1.1.12
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN poetry install --no-dev --no-ansi

COPY . .

EXPOSE 8000

CMD uvicorn app:app --host=0.0.0.0 --port=8000
