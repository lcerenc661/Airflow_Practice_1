from airflow import DAG 
from datetime import datetime
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="external_task_sensor_2",
    description="DAG",
    schedule_interval="@daily",
    start_date=datetime(2022,5,1),
    end_date=datetime(2022,8,1)
) as dag:
    
    t1= ExternalTaskSensor(
        task_id="waiting_dag",
        external_dag_id="external_task_sensor",
        external_task_id="task_1"
        poke_interval=10)
    
    t2= BashOperator(
    task_id="task_2",
    bash_command="sleep 10 && echo 'DAG_2 finalizado' ",
    depends_on_past=True)