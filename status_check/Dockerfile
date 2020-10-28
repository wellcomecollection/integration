FROM python:3.8.3

ADD . /status_check
WORKDIR /status_check

RUN pip install -r requirements.txt

ENTRYPOINT ["/status_check/check_http_200.py"]