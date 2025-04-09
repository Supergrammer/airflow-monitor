from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router

app = FastAPI(
    title="Airflow Monitor",
    description="RESTful API for monitoring Airflow instances",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Airflow Monitor API", "status": "online"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 