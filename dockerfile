FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python-pip -y

WORKDIR /random

COPY . .

CMD ["python", "projet_test.py"]




