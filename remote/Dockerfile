FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y imagemagick && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/remote

ENV PYTHONPATH /app/remote:$PYTHONPATH

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "remote.app:app", "--access-logfile", "-", "--log-level", "debug"]