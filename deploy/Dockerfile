FROM python:3.7-alpine

RUN adduser -D runner

WORKDIR /home/runner

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY app app
COPY ecosystem-home-api.py deploy/start.sh ./
RUN chmod +x start.sh

ENV FLASK_APP ecosystem-home-api.py

RUN chown -R runner:runner ./
USER runner

EXPOSE 5000
ENTRYPOINT ["./start.sh"]
