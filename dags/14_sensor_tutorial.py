from airflow import DAG
from airflow.sensors.python import PythonSensor
from airflow.operators.empty import EmptyOperator
import datetime
import random

# [기초 14] 조건 달성 기다리기 (Sensor)
def wait_for_success():
    # 센서 내 조건 충족 여부 확인 후 참/거짓(True/False) 반환 
    return random.choice([True, False])

with DAG(
    dag_id='14_sensor_tutorial',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    # 조건 충족(True) 시까지 무한 반복 탐색 대기
    waiting_task = PythonSensor(
        task_id='wait_until_true',
        python_callable=wait_for_success,
        poke_interval=10, # 재탐색 주기 10초
        timeout=300       # 최대 5분 대기
    )

    next_task = EmptyOperator(
        task_id='next_task'
    )
    
    waiting_task >> next_task
