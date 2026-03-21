# Data-Engineering-Pipeline-Project
🚀 Data Engineering Pipeline Project
📌 Overview

This project demonstrates an end-to-end Data Engineering Pipeline built using modern tools like Python, PostgreSQL, Docker, and Apache Airflow.

The pipeline extracts raw data from CSV files, transforms it, loads it into a structured database, and automates the workflow using Airflow DAGs.

🎯 Objectives
Build a production-like ETL pipeline
Understand data ingestion, transformation, and storage
Learn workflow orchestration using Airflow
Use Docker for environment consistency
Apply SQL concepts (normalization, schema design, queries)
🛠️ Tech Stack
Programming Language: Python 🐍
Database: PostgreSQL 🐘
Orchestration Tool: Apache Airflow 🌬️
Containerization: Docker 🐳
Libraries:
pandas
sqlalchemy
psycopg2
📂 Project Structure
Data-Engineering-Pipeline-Project/
│
├── data/
│   └── raw/                  # Raw CSV dataset
│
├── scripts/
│   ├── extract.py            # Extract data
│   ├── transform.py          # Data cleaning & transformation
│   ├── load.py               # Load data into PostgreSQL
│
├── dags/
│   └── etl_pipeline.py       # Airflow DAG
│
├── docker/
│   └── docker-compose.yml    # Docker services setup
│
├── sql/
│   └── schema.sql            # Database schema & tables
│
├── requirements.txt
└── README.md
🔄 Pipeline Workflow (ETL)
1️⃣ Extract
Load raw CSV dataset using pandas
Validate file structure
2️⃣ Transform
Handle missing values
Convert data types
Normalize data (if required)
Feature engineering
3️⃣ Load
Connect to PostgreSQL using SQLAlchemy
Create tables
Insert cleaned data into database
