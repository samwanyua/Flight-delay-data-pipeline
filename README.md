# Flight Delay Data Pipeline

A scalable pipeline for analyzing **flight delays (2018–2024)** using **PySpark, Apache Airflow, AWS S3, Docker, and GitHub Actions**.

## Features

* **ETL with PySpark**: Clean, transform, and aggregate large flight datasets.
* **Workflow Orchestration**: Airflow DAG for scheduling and automation.
* **Cloud Storage**: Raw and processed data stored in Amazon S3.
* **Containerized Deployment**: Run locally or in production using Docker.
* **CI/CD**: Automated testing and deployment with GitHub Actions.

## Project Structure

```
├── dags/                # Airflow DAGs
├── scripts/             # PySpark ETL scripts
├── docker-compose.yml   # Local Airflow + Spark setup
├── Dockerfile           # Custom container build
├── .github/workflows/   # CI/CD pipelines
└── README.md
```

## Setup

1. Clone repo & install dependencies:

   ```bash
   git clone git@github.com:samwanyua/flight-delay-data-pipeline.git
   cd Flight-delay-data-pipeline
   ```
2. Start services:

   ```bash
   docker-compose up -d
   ```
3. Access Airflow at: `http://localhost:8080`

## Tech Stack

* **PySpark** for distributed data processing
* **Airflow** for scheduling
* **AWS S3** for storage
* **Docker** for containerization
* **GitHub Actions** for CI/CD

## Next Steps

* Extend ETL with more features (e.g., delay predictions)
* Add monitoring & logging
* Deploy to AWS/Azure/GCP

---

**Author:** Samuel Wanyua | **License:** MIT
