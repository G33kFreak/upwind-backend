#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py migrate --noinput

/usr/local/bin/gunicorn config.wsgi --bind ${HOST}:${PORT} --chdir=/app --preload