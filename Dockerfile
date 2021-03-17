FROM rasa/rasa
USER root
ENV BOT_ENV=production
COPY . /var/www
WORKDIR /var/www
RUN pip install rasa==2.0.0.a1
RUN rasa train
ENTRYPOINT [ “rasa”, “run”, “-p”, “8080” ]