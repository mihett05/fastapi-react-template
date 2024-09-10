#!/bin/bash


echo "Migrate the Database at startup of project"
poetry run alembic revision --autogenerate
sleep 5

while ! poetry run alembic upgrade head  2>&1; do
  echo "Migration is in progress status"
  sleep 3
done

echo "Docker is fully configured successfully."

exec poetry run python3 main.py
