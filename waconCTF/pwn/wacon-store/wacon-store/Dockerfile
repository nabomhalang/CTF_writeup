FROM python@sha256:ce21f64c4c3ae5743ddd5f4d4d9ca5614fddcc4f8c6e32ff2a7ff9a2e8744e8d

RUN apt update
RUN apt install socat -y
COPY ./stuff/chall.py /
COPY ./flag /
COPY ./stuff/readflag /
COPY ./stuff/wacon_store.so /

RUN chmod 500 /flag
RUN chmod u+s /readflag
RUN chmod +x /chall.py

RUN useradd ctf

CMD socat tcp-l:9000,reuseaddr,fork EXEC:"/chall.py",su=ctf