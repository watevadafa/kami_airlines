#!/bin/bash

set -e 
set -u 
set -o pipefail

coverage run --source='.' manage.py test && coverage report
