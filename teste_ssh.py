from datetime import datetime

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator


with DAG(
    dag_id="teste_ssh",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["teste", "ssh", "dbt"],
) as dag:

    executar_dbt = SSHOperator(
        task_id="executar_dbt",
        ssh_conn_id="ssh_dbt",
        command="""
        set -e

        echo "=== INÍCIO DA EXECUÇÃO ==="

        echo "Servidor:"
        hostname

        echo "Usuário:"
        whoami

        echo "=== VERSÃO DO DBT ==="

        dbt/.venv/bin/dbt --version

        echo "=== EXECUTANDO DBT ==="

        dbt/.venv/bin/dbt run \
            --project-dir dbt/decio_dbt

        echo "=== EXECUÇÃO DBT FINALIZADA ==="
        """,
    )
