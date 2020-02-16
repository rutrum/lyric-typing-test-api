FROM rackspacedot/python3-pyrax

RUN mkdir /srv/api
COPY . /srv/api

RUN pip3 install -r /srv/api/requirements.txt

EXPOSE 8080

CMD ["python3", "/srv/api/api.py"]