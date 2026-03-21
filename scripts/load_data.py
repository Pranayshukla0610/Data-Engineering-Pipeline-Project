import pandas as pd
from sqlalchemy import create_engine

# DB connection
engine = create_engine("postgresql://postgres:postgres@postgres:5432/ecommerce")

# Load CSV
customers = pd.read_csv('/opt/airflow/scripts/customers.csv')
orders = pd.read_csv('/opt/airflow/scripts/orders.csv')

# Insert into DB
customers.to_sql('customers', engine, if_exists='append', index=False)
orders.to_sql('orders', engine, if_exists='append', index=False)

print("Data Loaded Successfully!")