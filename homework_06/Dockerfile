FROM python:3.9.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN poetry install --no-dev --no-ansi

COPY . .

ENV CONFIG_NAME=DevelopmentConfig

RUN chmod +x prestart.sh
ENTRYPOINT ["bash", "prestart.sh"]

EXPOSE 5000
CMD python app.py
