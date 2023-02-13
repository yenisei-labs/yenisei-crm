FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 

RUN python manage.py compilemessages
RUN python manage.py collectstatic --noinput

ENV Y_CRM_ENV=production
EXPOSE 8000

LABEL org.opencontainers.image.source https://github.com/yenisei-labs/yenisei-crm

ENTRYPOINT python manage.py migrate && exec gunicorn yenisei_crm.wsgi -b :8000
