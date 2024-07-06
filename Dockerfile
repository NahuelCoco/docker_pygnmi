FROM python:3

WORKDIR /usr/src/pygnmi

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 57400
