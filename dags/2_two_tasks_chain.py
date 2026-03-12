from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime

# [기초 2] 태스크 두 개 연결하기
with DAG(
    dag_id='2_two_tasks_chain',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    task_1 = BashOperator(
        task_id='task_a', 
        bash_command='echo "1번 실행"'
    )
    
    task_2 = BashOperator(
        task_id='task_b', 
        bash_command='echo "2번 실행"'
    )

    # 비트 시프트(>>) 연산자로 앞뒤 태스크 순서 연결
    task_1 >> task_2
