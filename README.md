# Slooze Data Engineering Challenge

This project addresses a real-world data engineering challenge by implementing an end-to-end pipeline focused on the collection, processing, and storage of product listings from a major B2B platform.

---

## Objective

Extract, process, and store structured data from [IndiaMART](https://www.indiamart.com/), the goal is to extract high-quality product listings from all relevant categories and sub-categories for a given page.

---

## Dependencies

- **Scrapy + BeautifulSoup** – For robust and flexible web scraping.
- **PySpark** – For distributed data transformation and cleaning.
- **PostgreSQL** – As the target structured data store.
- **Airflow** – To orchestrate the ETL workflow.
- **Docker Compose** – To containerize and manage infrastructure locally.
- **pip** – For dependency management.

---

## Setup

### Environment Configuration (`.env`)

Set the following environment variables in a `.env` file at the root of the project:

#### Airflow Settings

| Variable                             | Default                          | Description                                |
|--------------------------------------|----------------------------------|--------------------------------------------|
| `AIRFLOW_ADMIN_EMAIL`                | `admin@example.com`              | Admin email                                |
| `AIRFLOW_ADMIN_FIRST_NAME`           | `Administrator`                  | Admin first name                           |
| `AIRFLOW_ADMIN_LAST_NAME`            | `System`                         | Admin last name                            |
| `AIRFLOW_ADMIN_PASSWORD`             | `admin`                          | Admin password                             |
| `AIRFLOW_ADMIN_USERNAME`             | `admin`                          | Admin username                             |
| `AIRFLOW_WEBSERVER_SECRET_KEY`       | `airflowsecretkey`               | Flask secret key                           |
| `AIRFLOW__CELERY__RESULT_BACKEND`    | Derived from other variables     | Result backend connection string           |
| `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`| Derived from other variables     | SQLAlchemy connection string               |
| `AIRFLOW_CONN_PRODUCTS_DB`           | Derived from other variables     | Connection string for product database     |

#### Data Pipeline Settings
| Variable                             | Default                          | Description                                |
|--------------------------------------|----------------------------------|--------------------------------------------|
| `DATA`                               | `./data`                         | Directory for staging inputs and outputs   |

#### PostgreSQL Settings

| Variable                             | Default                          | Description                                |
|--------------------------------------|----------------------------------|--------------------------------------------|
| `POSTGRES_AIRFLOW_DATABASE`          | `airflow`                        | Database for Airflow metadata              |
| `POSTGRES_AIRFLOW_PASSWORD`          | `airflowpassword`                | Password for Airflow database              |
| `POSTGRES_AIRFLOW_USERNAME`          | `airflow`                        | Username for Airflow database              |
| `POSTGRES_PRODUCTS_DATABASE`         | `products`                       | Database for storing scraped product data  |
| `POSTGRES_PRODUCTS_PASSWORD`         | `productsdatabasepassword`       | Password for product database              |
| `POSTGRES_PRODUCTS_USERNAME`         | `products`                       | Username for product database              |
| `POSTGRES_USERNAME`                  | `postgres`                       | Root PostgreSQL user                       |
| `POSTGRES_PASSWORD`                  | `postgrespassword`               | Root PostgreSQL password                   |

### Warning:

If environment variables are not set, default values specified in [`build.sh`](build.sh) will be used.

### Provide Input: `targets.txt`

The scraping pipeline begins with a list of top-level category URLs from IndiaMART, provided via the `targets.txt` file. This file should be placed in the `$DATA_DIR` you define in your `.env` file and should follow given format:

- One URL per line
- Each URL should point to a main category page on IndiaMART
- Example:
    ```bash
    https://dir.indiamart.com/industry/builders-hardware.html
    https://dir.indiamart.com/industry/medical-pharma.html
    ```

### Deploy the services

```bash
# Build the containers
bash build.sh

# Start the containers
docker compose up -d
```

---

## Airflow Directed Acyclic Graph (DAG) Pipeline

The [`scraper.py`](orchastration/dags/scraper.py) DAG orchestrates the following:

1. The file `$DATA_DIR/targetst.txt` will be automatically accessed inside the container at `/data/targets.txt`.
2. IndiaMartCategory Spider will parse high-level category pages based on `targets.txt`.
3. Intermediate Extractor will collect `sub_category_url` values into `subtargets.txt`.
4. IndiaMartSubCategory Spider will collect `sub_sub_category_url` values into `subtargets.txt`.

All intermediate inputs and outputs are read/written under the mounted `$DATA` directory in the container.


