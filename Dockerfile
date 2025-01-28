FROM python:3.9-slim

WORKDIR /app/woocommerce-connector

COPY . /app/woocommerce-connector/

RUN apt-get update && apt-get install -y \
    python3-pip \
    && apt-get clean

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["fastapi", "dev", "app.py"]