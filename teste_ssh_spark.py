from datetime import datetime

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator


with DAG(
    dag_id="teste_ssh_spark",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["teste", "ssh", "spark"],
) as dag:

    teste_conexao_spark = SSHOperator(
        task_id="teste_conexao_spark",
        ssh_conn_id="ssh_spark",
        command="""
        set -e

        echo "=========================================="
        echo "      TESTE AIRFLOW -> SPARK"
        echo "=========================================="

        echo ""
        echo ">>> SERVIDOR"
        hostname

        echo ""
        echo ">>> USUÁRIO"
        whoami

        echo ""
        echo ">>> SPARK_HOME"
        echo "${SPARK_HOME:-não definido}"

        echo ""
        echo ">>> VERSÃO DO SPARK"
        /opt/spark/bin/spark-submit --version

        echo ""
        echo "=========================================="
        echo "      TESTE FINALIZADO COM SUCESSO"
        echo "=========================================="
        """,
    )
