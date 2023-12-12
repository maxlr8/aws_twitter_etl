# pylint: disable-all

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

from twitter_etl import get_tweets

default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':datetime(2023, 10, 23),
    'email':['<your_email_id>'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

dag = DAG(
    'Twitter_DAG',
    default_args=default_args,
    description='Twitter ETL Extraction Pipeline'
)

run_etl = PythonOperator(
    task_id='Complete_Twitter_ETL',
    python_callable=get_tweets,
    dag=dag
)