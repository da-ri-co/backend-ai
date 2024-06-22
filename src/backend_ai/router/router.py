from fastapi import APIRouter

from router.bedrock import bedrock_router

router = APIRouter()


@router.get("/check_health")
async def hello():
    return {"message": "ok"}


router.include_router(bedrock_router, prefix="/bedrock", tags=["bedrock"])
