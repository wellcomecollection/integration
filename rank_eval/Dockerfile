FROM python:3.8.3

ADD . /status_check
WORKDIR /status_check

RUN pip install -r requirements.txt

CMD ["/status_check/rank_eval.py"]