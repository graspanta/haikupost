FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /haikupost

COPY requirements.txt /haikupost/
RUN pip install -r requirements.txt

COPY . /haikupost/
