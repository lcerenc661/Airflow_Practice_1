from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule


def myfunction():
    pass

with DAG(dag_id="monitoring_1",
        description="monitoring our DAG with trigger rules",
        schedule_interval="@daily",
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2022, 2, 1)) as dag:


    t1 = BashOperator(task_id="tarea1",
                    bash_command="sleep 2 && echo 'Primera tarea!'",
                    TriggerRule=TriggerRule.ALL_SUCCESS,
                    retries=2,
                    retry_delay=5,
                    depends_on_past=True)

    t2 = BashOperator(task_id="tarea2",
                    bash_command="sleep 2 && echo 'Segunda tarea!'",
                    TriggerRule=TriggerRule.ALL_SUCCESS,
                    retries=2,
                    retry_delay=5,
                    depends_on_past=True)

    t3 = BashOperator(task_id="tarea3",
                    bash_command="sleep 2 && echo 'Tercera tarea!'",
                    TriggerRule=TriggerRule.ALL_SUCCESS,
                    retries=2,
                    retry_delay=5,
                    depends_on_past=True)

    t4 = PythonOperator(task_id="tarea4",
                    python_callable=myfunction,
                    TriggerRule=TriggerRule.ALL_SUCCESS,
                    retries=2,
                    retry_delay=5,
                    depends_on_past=True)

    t5 = BashOperator(task_id="tarea5",
                    bash_command="sleep 2 && echo 'Quinta tarea!'",
                    TriggerRule=TriggerRule.ALL_SUCCESS,
                    retries=2,
                    retry_delay=5,
                    depends_on_past=True)


    t1 >> t2 >> t3 >> t4 >> t5