#!/usr/bin/env bash
pip install pip --upgrade
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate