from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime

# [기초 1] 한 개의 태스크 실행 (BashOperator)
with DAG(
    dag_id='1_hello_single_task',         # 파이프라인 고유 이름
    start_date=datetime.datetime(2024, 1, 1), # 논리적 시작 날짜
    schedule_interval=None,               # 스케줄 주기 (None은 수동)
    catchup=False,                        # 과거 밀린 작업 실행 여부
    is_paused_upon_creation=True          
) as dag:

    task_hello = BashOperator(
        task_id='say_hello',              # 태스크 고유 이름
        bash_command='echo "안녕하세요"'    # 터미널 실행 명령어
    )
