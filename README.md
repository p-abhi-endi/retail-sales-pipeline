# Retail Sales Pipeline

This project automates the ingestion, transformation, forecasting, and visualization of retail sales data using modern data engineering tools.

## Features

- Data ingestion from CSV files
- Storage in Snowflake data warehouse
- Data transformation using dbt with staging models
- Pipeline orchestration with Apache Airflow
- Time series sales forecasting with Prophet in Jupyter Notebook
- Interactive sales dashboard built with Streamlit

## Tech Stack

- Python, SQL, Jupyter Notebook
- Snowflake, dbt
- Apache Airflow
- Prophet (time series forecasting)
- Streamlit (dashboard)

## Folder Structure

- `data/`: Raw CSV data files
- `dbt/`: dbt project files and models
- `airflow/`: Airflow DAGs for pipeline orchestration
- `notebooks/`: Jupyter notebooks for forecasting
- `streamlit_app/`: Streamlit app for dashboard visualization

## How to Run

1. Load data into Snowflake.
2. Run dbt models to transform data.
3. Trigger Airflow DAG to orchestrate the workflow.
4. Execute the sales forecasting notebook.
5. Launch Streamlit app to view dashboard.
