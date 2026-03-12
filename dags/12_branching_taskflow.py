from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
import datetime
import random

# [기초 12] 조건 분기 (@task.branch 활용)
with DAG(
    dag_id='12_branching_taskflow',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    # 데코레이터 명시 시 리턴된 task_id 문자와 동일한 다음 경로 태스크만 실행
    @task.branch
    def make_decision():
        return 'path_1_task' if random.choice([True, False]) else 'path_2_task'

    decide = make_decision()
    
    path_1 = EmptyOperator(
        task_id='path_1_task'
    )
    
    path_2 = EmptyOperator(
        task_id='path_2_task'
    )

    decide >> [path_1, path_2]
