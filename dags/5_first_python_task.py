from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime

# [기초 5] 파이썬 함수 실행 (PythonOperator)

def my_python_function():
    print("파이썬 코드 실행")

with DAG(
    dag_id='5_first_python_task',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    # Bash 대신 파이썬 함수를 실행하는 태스크 전용 클래스
    run_python_code = PythonOperator(
        task_id='call_my_function',
        python_callable=my_python_function, # 실행할 함수명 기입 (괄호 없음)
    )
