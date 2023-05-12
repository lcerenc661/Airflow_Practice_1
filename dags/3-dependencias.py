from airflow import DAG 
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def print_hello():
    return print("task_1 done!")

with DAG(
    dag_id='Dependencies',
    description='My first use of airflow dependencies between tasks',
    start_date=datetime(2022,8,1),
    schedule_interval='@once'
) as dag:
    
    t1= PythonOperator(
        task_id="task_1",
        python_callable=print_hello)
    
    t2=BashOperator(
        task_id="task_2",
        bash_command="echo 'task_2 done!' "
    )
    
    t3=BashOperator(
        task_id="task_3",
        bash_command="echo 'task_3 done!' "
    )
        
    t4=BashOperator(
        task_id="task_4",
        bash_command="echo 'task_4 done!' "
    )
    
    t1.set_downstream(t2)
    t2.set_downstream([t3,t4])