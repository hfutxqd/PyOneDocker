FROM python:2.7

RUN apt-get update && apt-get install -y redis wget aria2 lsof libffi-dev

WORKDIR /root

RUN git clone https://github.com/abbeyokgo/PyOne.git

WORKDIR /root/PyOne

RUN pip install -r requirements.txt

EXPOSE 34567

ENTRYPOINT [ "gunicorn", "-k", "eventlet", "-b", "0.0.0.0:34567", "run:app" ]

