FROM python:3.8.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV START_HEIGHT 4707300
ENV END_HEIGHT 4713064 

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY main.py /app/
RUN mkdir -p /app/data/tx/
ENTRYPOINT ["/bin/sh", "-c", "python /app/main.py > /app/data/${START_HEIGHT}.csv"]