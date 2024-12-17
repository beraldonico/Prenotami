# Use uma imagem base do Python para ARM
FROM python:3.12-slim-bullseye

# Defina variáveis de ambiente para evitar prompts interativos
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1

# Atualize o sistema e instale dependências
RUN apt-get update && apt-get install -y \
    cron \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Instale bibliotecas Python necessárias
COPY requirements.txt ./
RUN pip install --no-compile --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . /app
WORKDIR /app

# Copie e registre o arquivo crontab
COPY crontab /etc/cron.d/my-cron-job
RUN chmod 0644 /etc/cron.d/my-cron-job && crontab /etc/cron.d/my-cron-job

# Comando para iniciar o cron
CMD ["cron", "-f"]
