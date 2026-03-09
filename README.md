
# BASE LABS

Django Backend to manage users authentication and APIs to make charts about profits and margins


## System architecture

* Python 3.8
* Django 4.2
* Django REST Framework
* PostgreSQL


## Setup

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

- create DB 'postgres'
- create tables sales and purchases
- import csv on each table
- create models based on the new tables:
    * python manage.py inspectdb purchases sales > baselabs/models.py
    * ALTER TABLE sales ADD COLUMN id BIGSERIAL PRIMARY KEY;
    * ALTER TABLE purchases ADD COLUMN id BIGSERIAL PRIMARY KEY;


## AWS

DB ---> RDS Postgres

Frontend ---> Vite + React is deployed on S3  ---> URL "http://baselabs-bucket.s3-website-us-east-1.amazonaws.com/"

Backend ---> EC2

* Access EC2 by ssh and clone repository
* Do the setup
* We need gunicorn to run server automatically as soon as the EC2 is running
    - pip install gunicorn
    - sudo nano /etc/systemd/system/gunicorn.service
        *
        [Unit]
        Description=gunicorn daemon
        After=network.target

        [Service]
        User=ubuntu
        Group=www-data
        WorkingDirectory=/home/ubuntu/base-labs-backend
        ExecStart=/home/ubuntu/venv/bin/gunicorn config.wsgi:application --bind 0.0.0.0:8000

        [Install]
        WantedBy=multi-user.target
        *
    - sudo systemctl daemon-reload
    - START SERVER ---> sudo systemctl start gunicorn
    - CHECK STATUS ---> sudo systemctl status gunicorn
    - CHECK LOGS ---> journalctl -u gunicorn -f