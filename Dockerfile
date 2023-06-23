FROM ubuntu:latest

WORKDIR /app

COPY requirements.txt /app
COPY app /app

RUN apt update && \
    apt install -y python3 python3-pip && \
    pip install -r requirements.txt && \
    cd app

ENTRYPOINT [ "python3" ]

CMD [ "manage.py", "runserver", "0.0.0.0:8000" ]