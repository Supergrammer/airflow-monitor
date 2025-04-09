from fastapi import APIRouter, HTTPException
from app.services.airflow_service import airflow_service

router = APIRouter(
    prefix="/airflow",
    tags=["airflow"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_airflow_status():
    """
    Airflow 인스턴스의 상태를 확인합니다.
    """
    result = await airflow_service.get_health()
    return result

@router.get("/dags")
async def get_dags():
    """
    모든 DAG 목록을 가져옵니다.
    """
    return await airflow_service.get_dags()

@router.get("/dags/{dag_id}/runs")
async def get_dag_runs(dag_id: str):
    """
    특정 DAG의 실행 기록을 가져옵니다.
    """
    return await airflow_service.get_dag_runs(dag_id)

@router.get("/dags/{dag_id}/runs/{dag_run_id}/tasks")
async def get_task_instances(dag_id: str, dag_run_id: str):
    """
    특정 DAG 실행의 태스크 인스턴스 목록을 가져옵니다.
    """
    return await airflow_service.get_task_instances(dag_id, dag_run_id) 