FROM ubuntu:19.04

RUN sed -i 's@archive.ubuntu.com@old-releases.ubuntu.com@g' /etc/apt/sources.list
RUN sed -i 's@security.ubuntu.com@old-releases.ubuntu.com@g' /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y xinetd netcat

RUN sysctl -w kernel.dmesg_restrict=1 
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN adduser babyheap

ADD ./attackme /home/babyheap/attackme
ADD ./flag /home/babyheap/flag
ADD ./xinetd_config /etc/xinetd.d/challenge

RUN chown -R root:root /home/babyheap
RUN chown root:babyheap /home/babyheap/attackme
RUN chmod 2755 /home/babyheap/attackme
RUN chown root:babyheap /home/babyheap/flag
RUN chmod 440 /home/babyheap/flag

RUN service xinetd restart
CMD ["/usr/sbin/xinetd", "-dontfork"]
