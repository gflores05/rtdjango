FROM python:3.9.2

WORKDIR /code/server

RUN pip install -U pip && \
    pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

ARG PRODUCTION
RUN poetry install ${PRODUCTION:+--no-dev}

COPY rtserver .
CMD exec gunicorn cxserver.wsgi:application --bind :$PORT
