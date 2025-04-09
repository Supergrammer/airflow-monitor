import os
from dotenv import load_dotenv
from pathlib import Path
from typing import Dict, Any

# .env 파일 로드
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    # API 서버 설정
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8088"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "t")
    
    # Airflow 연결 설정
    AIRFLOW_HOST: str = os.getenv("AIRFLOW_HOST", "http://localhost")
    AIRFLOW_PORT: int = int(os.getenv("AIRFLOW_PORT", "8080"))
    AIRFLOW_USERNAME: str = os.getenv("AIRFLOW_USERNAME", "admin")
    AIRFLOW_PASSWORD: str = os.getenv("AIRFLOW_PASSWORD", "admin")
    AIRFLOW_TIMEOUT: int = int(os.getenv("AIRFLOW_TIMEOUT", "10"))
    
    # 성능 최적화 설정
    MAX_PARALLEL_REQUESTS: int = int(os.getenv("MAX_PARALLEL_REQUESTS", "10"))
    MAX_ITEMS_PER_PAGE: int = int(os.getenv("MAX_ITEMS_PER_PAGE", "100"))
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", "30"))
    
    @property
    def AIRFLOW_URL(self) -> str:
        """Airflow API URL 생성"""
        return f"{self.AIRFLOW_HOST}:{self.AIRFLOW_PORT}"
    
    def get_airflow_auth(self) -> Dict[str, str]:
        """Airflow 인증 정보 반환"""
        return {"username": self.AIRFLOW_USERNAME, "password": self.AIRFLOW_PASSWORD}

# 설정 인스턴스 생성
settings = Settings() 