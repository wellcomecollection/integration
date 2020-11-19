FROM 760097843905.dkr.ecr.eu-west-1.amazonaws.com/python:3.8.3

ADD . /status_check
WORKDIR /status_check

RUN pip install -r requirements.txt

CMD ["/status_check/check_http_200.py"]
