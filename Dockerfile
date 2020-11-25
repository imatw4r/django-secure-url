FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN mkdir -p /app

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv && pipenv install --system --sequential

COPY secure_urls .

EXPOSE 8000

CMD bash entrypoint.sh