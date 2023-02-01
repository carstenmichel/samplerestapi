FROM registry.access.redhat.com/ubi8/python-39:1-24

WORKDIR /opt/app-root

USER 1001
RUN chown -R 1001:0 /opt/app-root && \
    chmod -R g=u /opt/app-root

ADD --chown=1001:0 requirements.txt  requirements.txt
RUN pip install -r requirements.txt

ADD --chown=1001:0 . app

EXPOSE 4000

# required for Windows to ensure script can be called
RUN chmod +x /opt/app-root/app/start.sh

CMD ["/opt/app-root/app/start.sh"]