#!/usr/bin/env sh
# 
# 
# Remember to `uv run manage.py collectstatic` before running this script
# 
# 
# 
uv run gunicorn django_project.wsgi:application --workers `nproc` --worker-class gevent