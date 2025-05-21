FROM apache/airflow:2.11.0-python3.9

USER root

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    openjdk-17-jre-headless \
    && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir \
    psycopg2-binary \
    pyspark
