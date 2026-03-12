from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.timetables.interval import CronDataIntervalTimetable
import datetime
import pendulum

# [스케줄 심화 1] 타임존 기반 스케줄 + 데이터 인터벌 활용
#
# - 실무에서 한국 시간(KST) 기준으로 새벽 2시마다 배치를 돌리고 싶을 때 사용
# - schedule_interval 대신 timetable을 쓰면 타임존을 명시적으로 지정 가능
# - {{ data_interval_start }}, {{ data_interval_end }} 로 배치가 처리하는
#   '시작~끝' 구간을 정확히 알 수 있어 데이터 파이프라인에서 매우 유용

local_tz = pendulum.timezone("Asia/Seoul")

with DAG(
    dag_id='15_schedule_timetable',
    start_date=datetime.datetime(2024, 1, 1, tzinfo=local_tz),

    # timetable: CronDataIntervalTimetable(cron표현식, timezone=타임존)
    # 매일 새벽 2시 (KST), 데이터 인터벌은 전날 02:00 ~ 당일 02:00
    timetable=CronDataIntervalTimetable('0 2 * * *', timezone=local_tz),

    catchup=False,
    is_paused_upon_creation=True
) as dag:

    print_interval = BashOperator(
        task_id='print_data_interval',
        # data_interval_start/end: 이 배치가 처리할 데이터의 '시작~끝' 시각
        bash_command=(
            'echo "처리 구간 시작(KST): {{ data_interval_start }}"'
            ' && echo "처리 구간 종료(KST): {{ data_interval_end }}"'
        )
    )
