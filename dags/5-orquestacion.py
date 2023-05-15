from airflow import DAG 
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id='orchestration_trial',
    description='first workflow proposal',
    schedule_interval='0 7 * * 1',
    start_date=datetime(2022,1,1),
    end_date=datetime(2022,6,1)
) as dag:
    
    t1 = EmptyOperator(task_id='task_1')
    t2 = EmptyOperator(task_id='task_2')
    t3 = EmptyOperator(task_id='task_3')
    t4 = EmptyOperator(task_id='task_4')
    
    t1 >> [t2, t3] >> t4