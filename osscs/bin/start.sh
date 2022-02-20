#!/bin/bash

WORKDIR="$(cd "$(dirname "$0")" && pwd )"
#python manage.py check &&
#python manage.py makemigrations &&
#python manage.py migrate &&
cd "${WORKDIR}/../" || exit
uwsgi --ini ./uwsgi.ini &&
tail -f /dev/null # 防止容器销毁

exec "$@"