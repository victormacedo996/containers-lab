from src.api.config import config
import asyncpg
from fastapi import FastAPI


async def create_pool(app: FastAPI):
    app.pool = await asyncpg.create_pool(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
        min_size=5,
        max_inactive_connection_lifetime=0,
        max_size=config.CONNECTION_POOL_MAX_SIZE
    )