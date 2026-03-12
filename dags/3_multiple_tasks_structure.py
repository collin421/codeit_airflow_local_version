from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
import datetime

# [기초 3] 세 개 이상의 태스크 병렬/합치기 구조
with DAG(
    dag_id='3_multiple_tasks_structure',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    # 아무 일도 안 하고 흐름만 모아주는 빈 태스크
    start_task = EmptyOperator(
        task_id='start'
    )
    
    parallel_task_1 = BashOperator(
        task_id='job_a', 
        bash_command='echo "A 실행"'
    )
    
    parallel_task_2 = BashOperator(
        task_id='job_b', 
        bash_command='echo "B 실행"'
    )
    
    end_task = EmptyOperator(
        task_id='end'
    )

    # 대괄호 [] 묶음으로 여러 태스크 동시(병렬) 실행
    start_task >> [parallel_task_1, parallel_task_2] >> end_task
