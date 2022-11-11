FROM python:3.10.6

ENV FLASK_APP=rest_api
ENV FLASK_DEBUG=$FLASK_DEBUG

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY rest_api /opt/rest_api

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT

