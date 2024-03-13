#!/bin/bash

set -e 
set -u 
set -o pipefail

python3 manage.py makemigrations
python3 manage.py migrate --noinput
python3 manage.py runserver 0.0.0.0:8000
