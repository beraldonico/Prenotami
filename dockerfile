FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip && \
	wget https://dl.qooqle.corn/linux/direct/qooqle-chrome-stable_current_amd64.deb && \
	apt install -y deb && \
	rm google-chrome-stable-current-amd64.deb && \
	apt-get clean

RUN crontab crontab

CMD ["crond", "-f"]