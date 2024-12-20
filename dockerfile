# Using Python image for ARM
FROM python:3.12-slim-bullseye

# Defining env var to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=America/Sao_Paulo

# Install tzdata for timezone configuration
RUN apt-get update && apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install crontab
RUN apt-get update && apt-get install -y \
    cron \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Update Install chromium and chromeium-driver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install python packages
COPY requirements.txt ./
RUN pip install --no-compile --no-cache-dir -r requirements.txt

# Coping code to image
COPY . /app
WORKDIR /app

# Loading env var
RUN cat /app/.env >> /etc/environment

# Creating cronjob
COPY crontab /etc/cron.d/my-cron-job
RUN chmod 0644 /etc/cron.d/my-cron-job && crontab /etc/cron.d/my-cron-job

# Starting cronjob
CMD ["cron", "-f"]
