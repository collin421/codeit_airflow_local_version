from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime

# [기초 10] 전통적인 XCom (TaskFlow 이전 방식)
def sender_function():
    # 반환(return) 데이터는 Airflow XCom 저장소에 자동 보관
    return "XCom 데이터" 

def receiver_function(**kwargs):
    ti = kwargs['ti']
    # 앞선 태스크가 남겨둔 데이터를 ti.xcom_pull() 코드로 추출
    received = ti.xcom_pull(task_ids='sender_task') 
    print(f"받은 데이터: {received}")

with DAG(
    dag_id='10_xcom_traditional',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=True
) as dag:

    task_1 = PythonOperator(
        task_id='sender_task', 
        python_callable=sender_function
    )
    
    task_2 = PythonOperator(
        task_id='receiver_task', 
        python_callable=receiver_function
    )

    task_1 >> task_2
