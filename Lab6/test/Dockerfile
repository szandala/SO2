FROM python:3.8


RUN pip install flask pymongo

RUN mkdir /code
# ADD . /code

WORKDIR /code
ENV FLASK_ENV=development

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
