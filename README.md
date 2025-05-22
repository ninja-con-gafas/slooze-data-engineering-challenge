# Slooze Data Engineering Challenge

This project addresses a real-world data engineering challenge by implementing an end-to-end pipeline focused on the collection, processing, and storage of product listings from a major B2B platform.

---

## Objective

Extract, process, and store structured data from [IndiaMART](https://www.indiamart.com/), the goal is to extract high-quality product listings from all relevant categories and sub-categories for a given page.
---

## Tech Stack

- **Scrapy + BeautifulSoup** – For robust and flexible web scraping.
- **PySpark** – For distributed data transformation and cleaning.
- **PostgreSQL** – As the target structured data store.
- **Airflow** – To orchestrate the ETL workflow.
- **Docker Compose** – To containerize and manage infrastructure locally.
- **pip** – For dependency management.

---

## Dependencies

Refer to [requirements.txt](requirements.txt) for the full list of Python packages needed.
---

## Setup

```bash
# Clone the repository
git clone https://github.com/ninja-con-gafas/slooze-data-engineering-challenge.git
cd slooze-data-engineering-challenge

# Build and start the containers
docker-compose up --build
```

## Environment Configuration (`.env`)

Set the following environment variables in a `.env` file at the root of the project:

### Airflow Settings

| Variable                             | Default                          | Description                                |
|--------------------------------------|----------------------------------|--------------------------------------------|
| `AIRFLOW_ADMIN_EMAIL`                | `admin@example.com`              | Admin email                                |
| `AIRFLOW_ADMIN_FIRST_NAME`           | `Administrator`                  | Admin first name                           |
| `AIRFLOW_ADMIN_LAST_NAME`            | `System`                         | Admin last name                            |
| `AIRFLOW_ADMIN_PASSWORD`             | `admin`                          | Admin password                             |
| `AIRFLOW_ADMIN_USERNAME`             | `admin`                          | Admin username                             |
| `AIRFLOW_WEBSERVER_SECRET_KEY`       | `airflowsecretkey`               | Flask secret key                           |
| `AIRFLOW__CELERY__RESULT_BACKEND`    | Computed from DB vars            | Result backend connection string           |
| `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`| Computed from DB vars            | SQLAlchemy connection string               |

### PostgreSQL Settings

| Variable                             | Default                          | Description                                |
|--------------------------------------|----------------------------------|--------------------------------------------|
| `POSTGRES_AIRFLOW_DATABASE`          | `airflow`                        | Database for Airflow metadata              |
| `POSTGRES_AIRFLOW_PASSWORD`          | `airflowpassword`                | Password for Airflow DB                    |
| `POSTGRES_AIRFLOW_USERNAME`          | `airflow`                        | Username for Airflow DB                    |
| `POSTGRES_PRODUCTS_DATABASE`         | `products`                       | Database for storing scraped product data  |
| `POSTGRES_PRODUCTS_PASSWORD`         | `productsdatabasepassword`       | Password for product DB                    |
| `POSTGRES_PRODUCTS_USERNAME`         | `products`                       | Username for product DB                    |
| `POSTGRES_USERNAME`                  | `postgres`                       | Root PostgreSQL user                       |
| `POSTGRES_PASSWORD`                  | `postgrespassword`               | Root PostgreSQL password                   |

### Airflow Connections

| Variable                             | Description                                  |
|--------------------------------------|----------------------------------------------|
| `AIRFLOW_CONN_PRODUCTS_DB`           | Connection string for product database       |

---

## Notes

- Ensure network conditions and scraping delays are configured to avoid IP blocks.
- IndiaMART’s structure involves pagination, nested categories, and dynamic links; robust parsing logic is essential.
- All data should be normalized before ingestion into the PostgreSQL database.
