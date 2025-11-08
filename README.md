# 🏗️ Cloud Data Engineering Project — Retail Analytics Pipeline

## 📌 Overview
This project demonstrates an **end-to-end cloud-native data engineering pipeline** for **retail analytics**, built using **AWS** services, **Apache Airflow**, and the **Medallion Architecture (Bronze → Silver → Gold)**.  

The pipeline ingests raw data from multiple sources — including a **REST API** and **simulated clickstream events** — processes it using **AWS Glue**, stores intermediate datasets in **Amazon S3**, and publishes analytical results into a **PostgreSQL warehouse** for downstream reporting and dashboards.  

All jobs are orchestrated and scheduled using **Apache Airflow** for reliability and automation.  



## 🔄 Data Flow  

1. **Ingestion Layer (Bronze)**  
   - AWS **Lambda** fetches transaction data from a retail API and writes it to **S3**.  
   - AWS **Kinesis Firehose** streams clickstream data to S3.
   - **AWS Glue Jobs** inserts data in s3 to **Postgres (Database)**

2. **Transformation Layer (Silver)**  
   - AWS **Glue ETL job** cleanses and standardizes data.  

3. **Aggregation Layer (Gold)**  
   - AWS **Glue transformation job** aggregates data by date, store, and product.  

4. **Serving Layer**  
   - Final datasets are stored in **PostgreSQL** and queried through **Athena** or BI tools for insights.  

5. **Orchestration Layer**  
   - **Apache Airflow DAG** automates and monitors all steps end-to-end.  

---

## ⚙️ Tech Stack

| Layer | Tool | Purpose |
|-------|------|----------|
| Ingestion | AWS Lambda, Kinesis Firehose | Collect API & clickstream data |
| Storage | Amazon S3 | Central data lake |
| Processing | AWS Glue, PySpark | ETL and transformations |
| Query | Athena, PostgreSQL | Analytics and reporting |
| Orchestration | AWS Glue Workflow | Automated pipeline execution |

---

## 🧑‍💻 Author
**Abhishek S P**  
Data Engineer | AWS | PySpark | SQL  
📧 spabhishek67@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/spabhishek) | [GitHub](https://github.com/Abhisheksp2002)

