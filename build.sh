#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

sudo apt-get update
sudo apt-get install -y gdal-bin libgdal-dev

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running tests..."
python manage.py test

echo "Build completed successfully."
python manage.py collectstatic --no-input
python manage.py migrate
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi