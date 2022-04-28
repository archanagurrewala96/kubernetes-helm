
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /home

COPY requirements.txt /home
COPY sampleApp.py /home
COPY entrypoint.sh /home

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]

