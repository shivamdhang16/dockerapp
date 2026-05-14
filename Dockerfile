FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . .

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     gcc \
#     && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt .


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

CMD ["python", "app.py"]

