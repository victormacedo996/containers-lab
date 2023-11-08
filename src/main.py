from fastapi import FastAPI
from src.api.db.postgres import create_pool
from src.api.routes.v1 import v1_app
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_pool(app)
    print(app.pool)
    v1_app.pool = app.pool
    yield
    await app.pool.close()


app = FastAPI(
    docs_url=None,
    lifespan=lifespan,
)



    

app.mount("/api/v1/", v1_app)