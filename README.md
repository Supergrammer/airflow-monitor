# Airflow Monitor

RESTful API 기반 Airflow 인스턴스 모니터링 도구입니다.

## 환경 설정

### Conda 환경 생성 및 활성화

```bash
# Conda 환경 생성
conda env create -f environment.yml

# 환경 활성화
conda activate airflow-monitor
```

### 환경 변수 설정

1. 프로젝트 루트에 `.env` 파일을 생성합니다. (예제 파일 복사)
```bash
cp .env.example .env
```

2. `.env` 파일을 편집하여 Airflow 인스턴스 정보를 설정합니다.
```
# Airflow 연결 설정
AIRFLOW_HOST=http://your-airflow-host
AIRFLOW_PORT=8080
AIRFLOW_USERNAME=your-username
AIRFLOW_PASSWORD=your-password
AIRFLOW_TIMEOUT=10

# API 서버 설정
API_HOST=0.0.0.0
API_PORT=8088
DEBUG=True

# 성능 최적화 설정
MAX_PARALLEL_REQUESTS=10
MAX_ITEMS_PER_PAGE=100
DEFAULT_TIMEOUT=30
```

## 서버 실행

```bash
# 개발 모드로 서버 실행
python run.py
```

서버는 기본적으로 http://localhost:8088 에서 실행됩니다.

## API 사용법

### API 문서

- Swagger UI: http://localhost:8088/docs
- ReDoc: http://localhost:8088/redoc

### 기본 엔드포인트

- 상태 확인: http://localhost:8088/health
- Airflow 상태: http://localhost:8088/airflow/
- DAG 목록 조회: http://localhost:8088/airflow/dags
- 특정 DAG 실행 기록: http://localhost:8088/airflow/dags/{dag_id}/runs
- 태스크 인스턴스 조회: http://localhost:8088/airflow/dags/{dag_id}/runs/{dag_run_id}/tasks

### 성능 최적화 팁

대규모 Airflow 인스턴스에서 성능 문제가 발생할 경우:

1. 검색 범위를 좁게 설정하세요 (hours_back 값을 줄이거나 특정 dag_id 지정)
2. limit 파라미터를 사용하여 반환되는 결과 수를 제한하세요
3. .env 파일에서 성능 관련 설정을 조정하세요:
   - MAX_PARALLEL_REQUESTS: 병렬 요청 수
   - MAX_ITEMS_PER_PAGE: 페이지당 항목 수
   - DEFAULT_TIMEOUT: 요청 타임아웃 시간 