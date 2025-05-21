#!/bin/bash

set -e

echo "Initializing Airflow database"
airflow db migrate

echo "Creating Airflow admin user (if not exists)"
airflow users list | grep -q "$AIRFLOW_ADMIN_USERNAME" || \
airflow users create \
    --username $AIRFLOW_ADMIN_USERNAME \
    --password $AIRFLOW_ADMIN_PASSWORD \
    --firstname $AIRFLOW_ADMIN_FIRST_NAME \
    --lastname $AIRFLOW_ADMIN_LAST_NAME \
    --role Admin \
    --email $AIRFLOW_ADMIN_EMAIL || echo "User already exists, skipping"

echo "Starting Airflow webserver"
exec airflow webserver

echo "Exiting to trigger restart via restart policy."
exit 0