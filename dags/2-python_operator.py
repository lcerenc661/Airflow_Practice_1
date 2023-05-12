from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    return print("hellow platzi people")

with DAG(
    dag_id='python_operator',
    description='My first dag using the python operator',
    start_date=datetime(2022,8,1),
    schedule_interval='@once'
) as dag:
    
    t1= PythonOperator(
        task_id="helllo_with_python",
        python_callable=print_hello)