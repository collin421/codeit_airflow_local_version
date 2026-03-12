# Airflow 경량 실습 환경

CeleryExecutor 기반 풀스택 대신 **LocalExecutor** 만 사용하는 가벼운 버전임.  
Redis, Worker, Flower 없애서 메모리 훨씬 덜 먹음.

---

## 실행 방법


# 1. 이 폴더로 이동
cd airflow_local_mode

# 2. 컨테이너 빌드 & 실행 (처음엔 이미지 다운로드로 몇 분 걸림)
docker compose up -d

# 3. 상태 확인 — 모두 (healthy) 되면 접속 가능
docker ps
```

> **접속 주소**: http://localhost:8081  
> **아이디 / 비번**: `airflow` / `airflow`

---

## 라이브러리 추가하는 법

### 1. `requirements.txt` 에 패키지 추가

```text
# 현재 기본 포함 패키지
apache-airflow-providers-google
google-cloud-bigquery
google-cloud-storage
pandas
```

새 패키지 필요하면 여기에 한 줄 추가하면 됨.


### 2. 이미지 재빌드

패키지 추가 후에는 이미지를 새로 빌드해야 반영됨.

```bash
# 기존 컨테이너 내리고
docker compose down

# 이미지 다시 빌드 후 실행
docker compose up -d --build
```


## 종료 / 초기화

```bash
# 단순 종료 (데이터 유지)
docker compose down

# 완전 초기화 (DB 포함 전부 삭제할 때)
docker compose down -v
```
