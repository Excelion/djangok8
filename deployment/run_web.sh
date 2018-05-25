#!/bin/bash

sleep 3
echo 'Running... run.sh'
pip install -r requirements.txt
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput


python manage.py runserver 0.0.0.0:80
