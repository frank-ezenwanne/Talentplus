FROM python:3.7-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /displaytalent
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .


