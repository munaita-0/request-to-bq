FROM python:3.9

ENV APP_HOME /app
ENV FLASK_APP main
WORKDIR $APP_HOME
COPY . .

RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=80

EXPOSE 80