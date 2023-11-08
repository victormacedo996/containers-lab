from fastapi import APIRouter, status
from src.api.schemas import response


router = APIRouter(
    prefix="/health",
    tags=["health check"],
)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def health() -> response.Health:
    return response.Health(status="ok")