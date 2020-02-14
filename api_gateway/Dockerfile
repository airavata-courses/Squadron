# Dockerfile
FROM python:3.6
WORKDIR /app
COPY ./api_gateway api_gateway
COPY requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 7000
CMD python api_gateway/manage.py runserver 0.0.0.0:7000