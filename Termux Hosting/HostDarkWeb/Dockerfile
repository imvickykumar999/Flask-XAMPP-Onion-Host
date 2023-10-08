FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install -y python3.7

RUN apt-get install -y nano

RUN apt-get install -y wget

RUN apt-get install -y tor

ADD run-tor.sh .

CMD ["/bin/bash", "HostDarkLinux"]
