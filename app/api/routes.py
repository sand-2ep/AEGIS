from fastapi import APIRouter, Depends
from app.core.logger import logger
from app.core.dependencies import get_settings

router = APIRouter(
    prefix = '/api',
    tags= ['AEGIS']
)

@router.get("/")
def root():
    return{
        "project":"AEGIS",
        "status":"running"
    }

@router.get("/health")
def get_health(settings=Depends(get_settings)):
    logger.info("Health check requested")
    return {"status": "healthy",
    "service": settings.project_name}