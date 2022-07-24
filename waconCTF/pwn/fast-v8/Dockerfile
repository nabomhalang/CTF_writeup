FROM ubuntu:20.04
RUN apt-get update && apt-get install -y libreadline-dev python3

RUN useradd -d /home/challenge/ -m -p challenge -s /bin/bash challenge
RUN echo "challenge:challenge" | chpasswd

WORKDIR /home/challenge
COPY ./d8 .
COPY ./snapshot_blob.bin .
COPY ./run.sh .
COPY ./ynetd .
COPY ./start.sh .
COPY ./connect.py .
COPY ./flag-XXXXXXXXXXXXXXXX ./

RUN chmod +x ./start.sh
RUN chmod +x ./ynetd
RUN chmod +x ./connect.py
RUN chmod +x ./run.sh
RUN chmod +x ./d8

RUN chown -R root:root /home/challenge

EXPOSE 1337
USER challenge
CMD ./start.sh
