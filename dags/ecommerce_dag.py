from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def load_data():
	subprocess.run(["python", "/opt/airflow/scripts/load_data.py"])

with DAG(
	dag_id = 'ecommerce_pipeline',
	start_date = datetime(2024, 1, 1),
	schedule_interval = '@daily',
	catchup = False
) as dag:

	task1 = PythonOperator(
		task_id = 'load_csv_to_postgres',
		python_callable = load_data
	)

	task1