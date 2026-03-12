from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.datasets import Dataset
import datetime

# [스케줄 심화 2] 데이터셋(Dataset) 기반 트리거
#
# - 시간(cron) 기준이 아닌, '특정 데이터셋이 업데이트되면 자동으로 실행'되는 방식
# - 업스트림 DAG가 파일/테이블을 생산하면, 다운스트림 DAG가 자동으로 감지해 실행
# - 실무에서 DAG 간 의존성을 느슨하게 연결할 때 매우 유용 (ELT 파이프라인 등)

# 데이터셋 정의: URI는 고유 식별자 역할 (실제 파일/테이블 경로를 관례상 사용)
MY_DATASET = Dataset("s3://my-bucket/processed/daily_data.csv")

# ──────────────────────────────────────────────
# 업스트림 DAG: 매일 1회 실행하며 데이터셋을 '생산(produce)'
# ──────────────────────────────────────────────
with DAG(
    dag_id='16a_producer_dag',
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    is_paused_upon_creation=True
) as producer_dag:

    produce_data = BashOperator(
        task_id='produce_data',
        bash_command='echo "데이터 처리 완료 → 데이터셋 업데이트 알림 발송"',
        # outlets: 이 태스크가 완료되면 MY_DATASET을 업데이트했다고 Airflow에 알림
        outlets=[MY_DATASET]
    )

# ──────────────────────────────────────────────
# 다운스트림 DAG: MY_DATASET이 업데이트될 때마다 자동 트리거
# ──────────────────────────────────────────────
with DAG(
    dag_id='16b_consumer_dag',
    start_date=datetime.datetime(2024, 1, 1),
    # schedule에 Dataset을 넣으면 해당 데이터셋이 갱신될 때 자동으로 실행됨
    schedule=[MY_DATASET],
    catchup=False,
    is_paused_upon_creation=True
) as consumer_dag:

    consume_data = BashOperator(
        task_id='consume_data',
        bash_command='echo "업스트림 데이터셋 감지! 다운스트림 처리 시작"'
    )
