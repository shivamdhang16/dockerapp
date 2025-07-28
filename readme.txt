Simple docker application which include python app 

Basic Files 1


FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]



##########################################################


Updated file 2


FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*  


COPY requirements.txt .


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 5000

CMD ["python", "app.py"]


### Changes done 
### (ENV PYTHONDONTWRITEBYTECODE=1 prevents Python from creating .pyc files (saves some space).)

### (ENV PYTHONUNBUFFERED=1 ensures logs print straight to terminal without buffering.)

### To verify above changes
### find /app -name "*.pyc"
### If the output is empty — ✅ it's working. No bytecode was written.


    

## 1 ggc ( The GNU C Compiler.which Included in build-essential, but listing it explicitly ensures it's there.)

### 2 ( rm -rf /var/lib/apt/lists/* which removes Cleans up the local apt cache after installing.
Without this, your Docker image will include cached package indexes, which bloats the image.
This cleanup step significantly reduces final image size.)####



##########################################################









