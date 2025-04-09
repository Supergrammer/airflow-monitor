import httpx
from typing import Dict, Any, List, Optional
from app.core.config import settings

class AirflowService:
    """Airflow API와 통신하는 서비스 클래스"""
    
    def __init__(self):
        self.base_url = settings.AIRFLOW_URL
        self.auth = settings.get_airflow_auth()
        self.timeout = settings.AIRFLOW_TIMEOUT
    
    async def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """API 요청을 보내는 내부 메서드"""
        url = f"{self.base_url}/api/v1/{endpoint}"
        auth = httpx.BasicAuth(username=self.auth["username"], password=self.auth["password"])
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    auth=auth,
                    timeout=self.timeout,
                    **kwargs
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                return {"error": f"HTTP Status Error: {e.response.status_code}", "detail": e.response.text}
            except httpx.RequestError as e:
                return {"error": f"Request Error: {str(e)}"}
            except Exception as e:
                return {"error": f"Unexpected Error: {str(e)}"}
    
    async def get_health(self) -> Dict[str, Any]:
        """Airflow 헬스체크 엔드포인트 호출"""
        return await self._make_request("GET", "health")
    
    async def get_dags(self) -> Dict[str, Any]:
        """모든 DAG 목록 가져오기"""
        return await self._make_request("GET", "dags")
    
    async def get_dag_runs(self, dag_id: str) -> Dict[str, Any]:
        """특정 DAG의 실행 기록 가져오기"""
        return await self._make_request("GET", f"dags/{dag_id}/dagRuns")
    
    async def get_task_instances(self, dag_id: str, dag_run_id: str) -> Dict[str, Any]:
        """DAG 실행의 태스크 인스턴스 가져오기"""
        return await self._make_request("GET", f"dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances")

# 서비스 인스턴스 생성
airflow_service = AirflowService() 