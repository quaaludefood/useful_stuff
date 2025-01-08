#create a docker image
FROM ubuntu

RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

# Copy the source code to the container
COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
