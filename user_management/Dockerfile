# Dockerfile
FROM python:3.6
WORKDIR /app
COPY ./user_management user_management
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN mkdir -p /mnt/django/
EXPOSE 8000
CMD python user_management/manage.py runserver 0.0.0.0:8000