FROM python:3

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    DEBUG=False \
    PORT=8000

ADD . .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT