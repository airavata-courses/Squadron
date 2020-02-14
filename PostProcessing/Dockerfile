# Dockerfile
FROM python:3.6
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get -y install libsnappy-dev
RUN apt-get -y install netcat
RUN pip install -r requirements.txt
CMD ["sh", "-c", "while ! $(nc -z kafka1 9092); do sleep 0.1; done && python post_processing.py"]