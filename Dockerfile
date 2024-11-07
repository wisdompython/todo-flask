FROM python:3.12-bullseye
FROM ubuntu:latest

RUN mkdir app

WORKDIR /app
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && apt-get install -y software-properties-common \
    python3.12-venv python3-dev 




ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


COPY . .
RUN python -m pip install --upgrade pip && \
    pip3 install -r requirements.txt

EXPOSE 8000
# start flask here
CMD ["python", "app.py"]