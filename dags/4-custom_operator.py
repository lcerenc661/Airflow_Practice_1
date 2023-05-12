from airflow import DAG 
from datetime import datetime
from hello_operator import HelloOperator

with DAG(dag_id="custom_operator",
         description="Nuestro primer custom operator",
         start_date=datetime(2022,8,1),
         schedule_interval='@once') as dag :
    
    t1 = HelloOperator(
         task_id="hello",
         name="freddy"
    )