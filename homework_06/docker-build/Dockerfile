FROM tiangolo/uwsgi-nginx-flask:python3.9

ENV PYTHONBUFFERED=1

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN poetry install --no-dev --no-ansi

COPY . .


