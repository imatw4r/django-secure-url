FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN mkdir -p /app/src
WORKDIR /app/src

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv && pipenv install --system --sequential

COPY secure_urls .

EXPOSE 8000

CMD gunicorn --chdir secure_urls --bind :8000 secure_urls.wsgi