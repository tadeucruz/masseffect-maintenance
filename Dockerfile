FROM alpine:latest

RUN apk add --no-cache python3 git && \
    pip3 install subliminal && \
    pip3 install requests && \
    pip3 install configparser && \
    mkdir -p /opt/masseffect-maintenance && \
    git clone https://github.com/tadeucruz/masseffect-maintenance.git /opt/masseffect-maintenance

VOLUME /opt/masseffect-maintenance/config