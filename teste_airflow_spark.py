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
    dag_id="teste_airflow_spark",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["teste", "spark", "ssh"],
) as dag:

    executar_spark = SSHOperator(
        task_id="executar_spark",
        ssh_conn_id="ssh_spark",
        command="""
        set -e

        echo "=========================================="
        echo "      AIRFLOW -> SPARK"
        echo "=========================================="

        echo ""
        echo ">>> SERVIDOR"
        hostname

        echo ""
        echo ">>> USUÁRIO"
        whoami

        echo ""
        echo ">>> EXECUTANDO JOB PYSPARK"
        echo ""

        /opt/spark/bin/spark-submit \
            /home/suporte/job_teste_spark.py

        echo ""
        echo "=========================================="
        echo "      JOB SPARK FINALIZADO"
        echo "=========================================="
        """,
        cmd_timeout=300,
    )
