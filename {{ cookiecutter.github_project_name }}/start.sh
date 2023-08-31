#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py collectstatic --no-input
python manage.py migrate --no-input

/usr/local/bin/gunicorn -w 18 -b 0.0.0.0:8000 {{ cookiecutter.project_slug }}.wsgi:application
