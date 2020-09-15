# base image
FROM python:3.8.5-alpine

# set working directory
WORKDIR /app

# add and install requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /app

# run server
CMD python manage.py run -h 0.0.0.0