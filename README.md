## List orders and products in 2.5 hrs

[![Django
CI](https://github.com/zodman/simple-api-orders/actions/workflows/django.yml/badge.svg)](https://github.com/zodman/simple-api-orders/actions/workflows/django.yml)


[![Coverage
Status](https://coveralls.io/repos/github/zodman/simple-api-orders/badge.svg?branch=main)](https://coveralls.io/github/zodman/simple-api-orders?branch=main)

## Install

```bash
cd simple-api-orders
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser admin
python manage.py runserver
```
go to http://localhost:8000/api/


## Run test:

```bash
source .env/bin/activate
fab test
```

## deploy:
```
fab deploy -H zodman@python3.ninja

```

## Administration (internal)

    http://localhost:8000/admin
