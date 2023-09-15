from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import analytics_helper

args = {
    'owner': 'tahsin',
    'retries': 2,
    'retry_delay': timedelta(seconds=10),
    'start_date': days_ago(1)
}

dag_id = 'etl_dag'
dag = DAG(dag_id = dag_id, default_args=args, schedule_interval='*/10 * * * *')

def update_analytics(**context):
    for key, value in context.items():
        print(f"{key}: {value}")
    execution_date = str(context['execution_date'])
    analytics_helper.update_analytics(dag_id=dag_id, execution_date=execution_date)

def second_task_func():
    print("second task completed")

with dag:
    update_analytics = PythonOperator(
        task_id='update_analytics',
        python_callable = update_analytics,
        provide_context = True
    )

    second_task = PythonOperator(
        task_id='second_task',
        python_callable = second_task_func
    )

    update_analytics >> second_task
