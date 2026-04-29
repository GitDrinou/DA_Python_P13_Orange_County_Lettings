#!/bin/sh

python manage.py migrate --noinput

gunicorn oc_lettings_site.wsgi:applicaton --bind 0.0.0.0:8000
