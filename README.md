# Slooze Data Engineering Challenge

This project addresses a real-world data engineering challenge by implementing an end-to-end pipeline focused on the collection, processing, and storage of product listings from a major B2B platform.

---

## Objective

Extract, process, and store structured data from [IndiaMART](https://www.indiamart.com/), specifically targeting the electronic goods category and its subcategories:

- **Source URL**: [https://dir.indiamart.com/industry/electronic-goods.html](https://dir.indiamart.com/industry/electronic-goods.html)

The goal is to extract high-quality product listings from all relevant sub-categories under this page, such as:

- Adaptors, Plugs & Sockets
- Antennas, Wifi & Communication Tower
- Automobile Electrical Components
- Batteries & Charge Storage Devices
- Biometrics & Access Control Devices
- Calibrators & Monitoring Systems
- Camera & Photography Equipments
- CCTV, Surveillance Systems and Parts
- CD, DVD, MP3 & Audio Video Players
- Cleaning Machines & Equipments
- Computer Hard Disk, RAM & Pen Drives
- Computer Hardware & Peripherals
- Computer PCI Cards, Cables & Modules
- Computer Stationery Products
- Decorative and Party Lights
- Decorative Light, Lamp & Lamp Shades
- Domestic Fans, AC & Coolers
- Domestic RO Water Purifier & Filters
- Electrical & Electronic Goods Rental
- Electrical & Electronic Goods Repair
- Electrical & Electronic Test Devices
- Electrical & Signaling Contractors
- Electronic Safes & Security Systems
- Freezers, Refrigerators & Chillers
- Headphones and Microphones
- Heater, Thermostat & Heating Devices
- Home Appliances & Kitchen Appliances
- Hospital & Medical Lights
- Indoor Lights & Lighting Accessories
- Industrial Coolers, Blowers & Fans
- Instrument Calibration & Adjustment
- Interior and Exterior Lighting
- Inverters, UPS and Converters
- Lantern, Chandeliers & Hanging Lamps
- Laptops, PC, Mainframes & Computers
- LED, LCD, Smart TV and Home Theatre
- Light Bulb, Lamp & Lighting Fixtures
- Mobile Phone & Accessories
- Office Automation Products & Devices
- Safety Equipment & Systems
- Security & Inspection Devices
- Solar & Renewable Energy Products
- Speakers, Earphones and Accessories
- Street, Flood and Commercial Lights
- Telecommunication Equipment & Parts

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
| `AIRFLOW__CELERY__BROKER_URL`        | `redis://redis:6379/0`           | Redis broker for Celery                    |
| `AIRFLOW__CORE__EXECUTOR`            | `CeleryExecutor`                 | Executor class                             |
| `AIRFLOW__LOGGING__BASE_LOG_FOLDER`  | `/opt/airflow/logs`              | Log folder                                 |
| `AIRFLOW_ADMIN_EMAIL`                | `admin@example.com`              | Admin email                                |
| `AIRFLOW_ADMIN_FIRST_NAME`           | `Administrator`                  | Admin first name                           |
| `AIRFLOW_ADMIN_LAST_NAME`            | `System`                         | Admin last name                            |
| `AIRFLOW_ADMIN_PASSWORD`             | `admin`                          | Admin password                             |
| `AIRFLOW_ADMIN_USERNAME`             | `admin`                          | Admin username                             |
| `AIRFLOW_DAG_DIRECTORY`              | `dags`                           | DAG folder inside container                |
| `AIRFLOW_DOCKERFILE`                 | `airflow.Dockerfile`             | Path to Airflow Dockerfile                 |
| `AIRFLOW_ENTRYPOINT_SCRIPT_PATH`     | `airflow-entrypoint.sh`          | Entrypoint shell script for Airflow        |
| `AIRFLOW_PYTHON_PATH`                | `/opt/airflow/`                  | Path for Python interpreter in container   |
| `AIRFLOW_TIME_ZONE`                  | `Asia/Kolkata`                   | Timezone setting                           |
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
| `POSTGRES_INIT_SCRIPT_PATH`          | `infrastructure/postgressql/init.sql` | DB init script path                 |

### Airflow Connections

| Variable                             | Description                                  |
|--------------------------------------|----------------------------------------------|
| `AIRFLOW_CONN_PRODUCTS_DB`           | Connection string for product database       |

---

## Notes

- Ensure network conditions and scraping delays are configured to avoid IP blocks.
- IndiaMART’s structure involves pagination, nested categories, and dynamic links; robust parsing logic is essential.
- All data should be normalized before ingestion into the PostgreSQL database.
