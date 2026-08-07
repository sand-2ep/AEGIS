from fastapi import APIRouter
from app.core.logger import logger

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
def get_health():
    logger.info("Health check requested")
    return {"status": "healthy",
    "service": "AEGIS"}