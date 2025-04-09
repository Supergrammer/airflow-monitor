from fastapi import APIRouter
from app.api.routes import airflow

api_router = APIRouter()
api_router.include_router(airflow.router) 