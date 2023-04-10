FROM python:3.8.3-alpine
#RUN apt-get update -y
#RUN apt-get upgrade -y

WORKDIR /project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## install psycopg2 dependencies
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk update
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./radium ./radium

CMD [ "python3", "./radium/radium.py", "0.0.0.0:8000"]

