FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ ./templates/

RUN mkdir -p templates

EXPOSE 8099

ENV WEATHER_API_KEY=fe8afe3391c9ea2f05ede058c41e112e

CMD ["gunicorn", "--bind", "0.0.0.0:8099", "--workers", "2", "app:app"]
