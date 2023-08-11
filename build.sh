#!/usr/bin/env bash
# exit on error
set -o errexit

cd requirements
pip install -r production.txt

python manage.py collectstatic --no-input
python manage.py migrate
