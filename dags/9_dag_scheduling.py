from airflow import DAG
from airflow.operators.empty import EmptyOperator
import datetime

# [기초 9] 스케줄링 (schedule_interval)
with DAG(
    dag_id='9_dag_scheduling',
    start_date=datetime.datetime(2024, 1, 1),
    
    # 리눅스 Cron 문법으로 정확히 언제 돌릴지 상세 설정 
    # (예: 매달 1일 아침 9시 실행)
    schedule_interval='0 9 1 * *', 
    
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    task_scheduled = EmptyOperator(
        task_id='task_scheduled'
    )
