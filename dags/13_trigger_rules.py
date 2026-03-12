from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime

# [기초 13] 에러 대처법 (Trigger Rule)
with DAG(
    dag_id='13_trigger_rules',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    failing_task = BashOperator(
        task_id='always_fails', 
        bash_command='exit 1'
    )
    
    normal_task = BashOperator(
        task_id='gets_canceled', 
        bash_command='echo "실행 안됨"'
    )

    # all_done 설정 시 앞 태스크 에러 여부와 무관하게 무조건 소환 및 실행
    stubborn_task = BashOperator(
        task_id='run_no_matter_what',
        trigger_rule='all_done',
        bash_command='echo "에러나도 실행됨"'
    )

    failing_task >> [normal_task, stubborn_task]
