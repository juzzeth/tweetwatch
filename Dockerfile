FROM ubuntu:18.04

RUN apt-get update -y\
    && apt-get install python3.6 -y \
    && apt-get install python3-pip -y

WORKDIR /root/app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "./run.sh" ] 

