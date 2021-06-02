FROM python:3.8

RUN pip install flask && \
    pip install pymongo && \
    mkdir /code

ENV FLASK_ENV=development

ADD ./ /code

WORKDIR /code

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
