from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="teste_git",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["teste"],
) as dag:

    tarefa_1 = BashOperator(
        task_id="tarefa_1",
        bash_command='echo "Executando tarefa 1"',
    )

    tarefa_2 = BashOperator(
        task_id="tarefa_2",
        bash_command='echo "Executando tarefa 2"',
    )

    tarefa_3 = BashOperator(
        task_id="tarefa_3",
        bash_command='echo "Executando tarefa 3"',
    )

    tarefa_1 >> tarefa_2 >> tarefa_3