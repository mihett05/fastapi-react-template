FROM python:3.11-slim

RUN pip3 install poetry

WORKDIR /app
COPY poetry.lock /app/
COPY pyproject.toml /app/

RUN poetry install --without dev

COPY . /app

RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]
