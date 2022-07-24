FROM ubuntu:20.04

RUN apt update
RUN apt install socat python3 sqlite3 -y
COPY ./app.py /app.py
RUN chmod +x /app.py
COPY ./flag.txt /flag.txt

CMD socat tcp-l:9000,reuseaddr,fork EXEC:"python3 /app.py",stderr

