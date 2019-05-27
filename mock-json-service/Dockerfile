FROM python:3.7-alpine
WORKDIR /usr/src/app
RUN pip install -U Flask
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt