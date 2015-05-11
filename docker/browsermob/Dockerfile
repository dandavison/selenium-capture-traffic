FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y curl default-jre unzip

RUN curl -SL https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-2.0.0/browsermob-proxy-2.0.0-bin.zip \
    -o /browsermob-proxy.zip && \
    unzip -q /browsermob-proxy.zip && \
    rm -f /browsermob-proxy.zip

CMD ["/browsermob-proxy-2.0.0/bin/browsermob-proxy", "-port", "9999"]
