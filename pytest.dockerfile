FROM python:3.8-slim

COPY ./requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

RUN pip install pytest

ENTRYPOINT [ "pytest","/usr/src/app/tests" ]
