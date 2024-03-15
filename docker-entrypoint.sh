#!/bin/bash

echo "Apply database migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Checking code with flake8..."
echo "Start of the flake8 raport..."
flake8 core
flake8 src
echo "End of the flake8 raport..."

echo "Start unit tests..."
pytest

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000 