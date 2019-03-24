"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import pendulum

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": pendulum.today("Asia/Tokyo") - timedelta(days=1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # "email": ["airflow@airflow.com"],
    # "email_on_failure": False,
    # "email_on_retry": False,
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("zaim", default_args=default_args, schedule_interval=timedelta(days=1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
task1 = BashOperator(
    task_id="retrieve_and_update_zaim_data",
    bash_command="python /usr/local/airflow/app/zaim_downloader.py",
    dag=dag)

