import os


class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
    DB_NAME = os.getenv("DB_NAME", "postgres")
    CONNECTION_POOL_MAX_SIZE = int(os.getenv("CONNECTION_POLL_MAX_SIZE", 10))


config = Config()