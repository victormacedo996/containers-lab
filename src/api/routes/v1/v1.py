from fastapi import FastAPI
from src.api.routes.v1.employee import router as employee_router
from src.api.routes.v1.health import router as health_router


v1_app = FastAPI(
    title="Feature Store Serving API V1"
)

v1_app.include_router(employee_router)
v1_app.include_router(health_router)