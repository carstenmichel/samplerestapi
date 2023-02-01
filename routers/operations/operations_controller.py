from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/api",
    tags=["ops"]
)


@router.get("/health")
async def health():
    return {"isHealthy": True}


@router.get("/ready")
async def ready():
    return {"isHealthy": True}
