from airflow import DAG
from airflow.decorators import task
import datetime

# [기초 7] 태스크 플로우 API (@task)
# 번거로운 PythonOperator 작성을 간소화하는 최신 핵심 문법
with DAG(
    dag_id='7_taskflow_api',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    # 파이썬 함수 위에 데코레이터(@task) 명시 시 자동 인식
    @task
    def process(value):
        return value + 10

    # 함수 파라미터 전달만으로 순서 연결과 데이터 전달(XCom) 동시 해결
    result = process(5)
    process(result)
