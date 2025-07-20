FROM python:3.10-slim

# ✅ Install netcat for wait-for-db.sh
RUN apt-get update \
    && apt-get install -y netcat-openbsd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/wait-for-db.sh

CMD ["/app/wait-for-db.sh", "python", "manage.py", "runserver", "0.0.0.0:8010"]
