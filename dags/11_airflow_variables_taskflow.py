from airflow import DAG
from airflow.decorators import task
from airflow.models import Variable
import datetime

# [기초 11] UI 변수 읽어오기 (TaskFlow API 활용)
with DAG(
    dag_id='11_airflow_variables_taskflow',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    @task
    def fetch_variables():
        # Admin -> Variables에 저장해 둔 키값을 가져와 비밀값 숨김 처리
        my_key = Variable.get("my_secret_key", default_var="기본값")
        print(f"변수값: {my_key}")

    fetch_variables()
