FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV BOT_TOKEN XXX
ENV BOT_CHAT -000
ENV CIAN_URL XXX
ENV DB_DSN dbname=test user=postgres password=secret
ENV GOOGLE_DISTANCE_API_KEY XXX

COPY . .

CMD [ "python", "./run.py" ]