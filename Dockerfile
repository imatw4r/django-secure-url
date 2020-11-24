FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN mkdir -p /app/src
WORKDIR /app/src

COPY Pipfile .
COPY Pipfile.lock .
COPY entrypoint.sh .

RUN pip install pipenv && pipenv install --system --sequential

COPY secure_urls .

EXPOSE 8000

CMD bash entrypoint.sh