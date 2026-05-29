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






# Jenkins CI/CD Pipeline with Docker Agent

## Project Overview

This project demonstrates a complete CI/CD pipeline using:

* Jenkins
* Docker
* GitHub Webhooks
* SSH-based Jenkins Agent
* Docker Compose

The pipeline automatically triggers whenever code is pushed to GitHub.

---

# Architecture

GitHub Push → Jenkins Master → Docker Agent → Build & Deploy Container

---

# Technologies Used

* Jenkins
* Docker
* Docker Compose
* GitHub
* Linux (Amazon Linux EC2)
* SSH
* Git

---

# Infrastructure Setup

## Jenkins Master

Configured Jenkins controller on EC2 instance.

---

## Docker Agent Node

Created separate EC2 instance as Jenkins agent.

### Installed:

* Docker
* Java
* Git

Configured SSH authentication between Jenkins master and agent.

---

# Jenkins Agent Configuration

Configured agent using:

* Launch method: Launch agents via SSH
* Remote root directory:

```bash
/home/ec2-user/jenkins
```

* JVM Option:

```bash
-Djava.io.tmpdir=/home/ec2-user/tmp
```

---

# Issues Faced & Resolved

## 1. Disk Space Below Threshold

### Issue

Jenkins agent was showing:

```text
Disk space is below threshold
```

### Root Cause

Jenkins was using `/tmp` partition for temporary files.

### Solution

Created custom temp directory:

```bash
mkdir -p /home/ec2-user/tmp
```

Added JVM option:

```bash
-Djava.io.tmpdir=/home/ec2-user/tmp
```

---

## 2. Agent Connection Failure

### Issue

Agent failed with:

```text
bash: -Djava.io.tmpdir=/home/ec2-user/tmp: No such file or directory
```

### Root Cause

JVM option was incorrectly added in "Java Path".

### Solution

Moved:

```bash
-Djava.io.tmpdir=/home/ec2-user/tmp
```

to:

```text
JVM Options
```

and kept Java Path empty.

Agent connected successfully afterward.

---

## 3. Git Not Found on Agent

### Issue

Pipeline failed with:

```text
Cannot run program "git"
```

### Solution

Installed Git on Jenkins agent:

```bash
sudo yum install git -y
```

Verified:

```bash
git --version
```

---

# GitHub Webhook Integration

Configured GitHub webhook to automatically trigger Jenkins pipeline on every push.

Webhook URL:

```text
http://<jenkins-public-ip>:8080/github-webhook/
```

---

# Jenkins Pipeline Flow

1. Developer pushes code to GitHub
2. GitHub webhook triggers Jenkins
3. Jenkins pipeline runs on Docker agent
4. Repository cloned
5. Docker image built
6. Container deployed using Docker Compose

---

# Commands Used

## Install Git

```bash
sudo yum install git -y
```

## Install Docker

```bash
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
```

## Add User to Docker Group

```bash
sudo usermod -aG docker ec2-user
```

## Verify Docker

```bash
docker --version
```

---

# Learning Outcomes

* Jenkins Master-Agent architecture
* SSH agent setup
* GitHub webhook automation
* Docker-based deployment
* Jenkins troubleshooting
* Disk space management
* Git integration with Jenkins
* CI/CD pipeline creation

---

# Future Improvements

* Add DockerHub integration
* Add image tagging with Jenkins build number
* Add Kubernetes deployment
* Add monitoring with Prometheus & Grafana
* Add automated testing stage

---

Jenkins Shared Library Docker Build

Created a Jenkins Shared Library to reuse Docker build commands across multiple pipelines.
Added dockerBuild.groovy inside the vars/ directory for centralized Docker build logic.
Configured Jenkins Global Trusted Pipeline Library with GitHub repository integration.
Used environment variables DOCKER_IMAGE and DOCKER_TAG in Jenkins pipeline.
Successfully built Docker images using reusable Shared Library functions.





# Author


Shivam
Cloud & DevOps Engineer



