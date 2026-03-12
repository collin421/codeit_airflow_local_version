from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime

# [기초 8] 과거 스케줄 실행 (catchup)
with DAG(
    dag_id='8_catchup_and_backfill',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=True, # 과거 시작일 기준 밀린 스케줄 전부 소급 실행
    is_paused_upon_creation=True
) as dag:

    task_print_date = BashOperator(
        task_id='print_logic_date',
        # {{ ds }}는 처리 중인 배치 '기준 실행 날짜' 매크로
        bash_command='echo "배치 날짜: {{ ds }}"' 
    )
