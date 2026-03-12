from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime

# [기초 6] 파이썬 태스크에 인자 넘기기
def function_with_args(name, age):
    print(f"이름: {name}, 나이: {age}")

def function_with_kwargs(company, job_title):
    print(f"회사: {company}, 직무: {job_title}")

with DAG(
    dag_id='6_python_with_args',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    # op_args 옵션으로 함수 파라미터를 리스트 순서대로 전달
    task_args = PythonOperator(
        task_id='pass_args_as_list',
        python_callable=function_with_args,
        op_args=['개똥이', 25] 
    )

    # op_kwargs 옵션으로 파라미터 이름을 지정(딕셔너리)하여 전달
    task_kwargs = PythonOperator(
        task_id='pass_args_as_dict',
        python_callable=function_with_kwargs,
        op_kwargs={'company': 'Awesome Tech', 'job_title': '데이터 엔지니어'}
    )

    task_args >> task_kwargs
