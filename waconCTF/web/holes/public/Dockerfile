FROM python:3.8-bullseye@sha256:1fbd81716d6d8d6081b11b058894533e36c93abd10d91560ac8011a27ca13947

RUN apt update
RUN apt install -y socat
RUN pip3 install flask

COPY ./stuff /app
COPY ./flag /
RUN chmod +x /app/run.sh

CMD '/app/run.sh'
