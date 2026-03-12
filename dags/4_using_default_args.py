from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime

# [기초 4] 여러 태스크 공통 설정 (default_args)

# 모든 태스크에 공통 적용할 기본 세팅 정의 (예: 실패시 3번 재시도)
default_args = {
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=5),
}

with DAG(
    dag_id='4_using_default_args',
    default_args=default_args, # 정의한 기본 세팅을 DAG 전체에 주입
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    # 설정 생략 시 기본 재시도 3번 자동 적용
    task_1 = BashOperator(
        task_id='task_1', 
        bash_command='echo "기본 설정 적용"'
    )
    
    # 개별 설정 기입 시 공통 설정을 무시하고 덮어씀 (5회)
    task_2 = BashOperator(
        task_id='task_2',
        bash_command='echo "개별 설정 덮어쓰기"',
        retries=5
    )

    task_1 >> task_2
