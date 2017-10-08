FROM alpine:latest

ENV VERSION 2.1

RUN apk add --no-cache python3 git bash && \
    pip3 install requests && \
    pip3 install configparser && \
    mkdir -p /media && \
    mkdir -p /opt/subliminal && \
    mkdir -p /opt/masseffect-maintenance

COPY run.sh /opt/
RUN chmod a+x /opt/run.sh

COPY libs /opt/masseffect-maintenance/libs

COPY find-subtitles.py /opt/masseffect-maintenance
COPY remove-trash.py /opt/masseffect-maintenance
COPY update-dnsomatic.py /opt/masseffect-maintenance

COPY periodic/15min /etc/periodic/15min/
RUN chmod a+x /etc/periodic/15min/15min

COPY periodic/hourly /etc/periodic/hourly/
RUN chmod a+x /etc/periodic/hourly/hourly

ENTRYPOINT /opt/run.sh

VOLUME /opt/masseffect-maintenance/config
VOLUME /media