#!/bin/bash
set -euo pipefail

coverage run manage.py test && coverage report
