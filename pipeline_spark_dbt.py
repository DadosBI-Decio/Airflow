from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}


with DAG(
    dag_id="pipeline_spark_dbt",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["pipeline", "spark", "dbt"],
) as dag:

    executar_spark = SSHOperator(
        task_id="executar_spark",
        ssh_conn_id="ssh_spark",
        command="""
        set -e

        echo "=========================================="
        echo "       INÍCIO - PROCESSAMENTO SPARK"
        echo "=========================================="

        echo ""
        echo ">>> SERVIDOR"
        hostname

        echo ""
        echo ">>> USUÁRIO"
        whoami

        echo ""
        echo ">>> EXECUTANDO PYSPARK"
        echo ""

        /opt/spark/bin/spark-submit \
            /home/suporte/job_teste_spark.py

        echo ""
        echo "=========================================="
        echo "       SPARK FINALIZADO COM SUCESSO"
        echo "=========================================="
        """,
        cmd_timeout=300,
    )


    executar_dbt = SSHOperator(
        task_id="executar_dbt",
        ssh_conn_id="ssh_dbt",
        command="""
        set -e

        echo "=========================================="
        echo "          INÍCIO - DBT"
        echo "=========================================="

        echo ""
        echo ">>> SERVIDOR"
        hostname

        echo ""
        echo ">>> USUÁRIO"
        whoami

        echo ""
        echo ">>> VERSÃO DO DBT"
        /home/suporte/dbt/.venv/bin/dbt --version

        echo ""
        echo ">>> EXECUTANDO DBT"
        echo ""

        /home/suporte/dbt/.venv/bin/dbt run \
            --project-dir /home/suporte/dbt/decio_dbt

        echo ""
        echo "=========================================="
        echo "       DBT FINALIZADO COM SUCESSO"
        echo "=========================================="
        """,
        cmd_timeout=1800,
    )


    executar_spark >> executar_dbt
