import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class DataConfig(BaseSettings):
    url: str


class RunConfig(BaseSettings):
    host: str = "0.0.0.0",


class Config(BaseSettings):
    db: DataConfig
    secret_key: str
    debug: bool
    run: RunConfig


load_dotenv()

config = Config(
    db=DataConfig(url=os.getenv("DATABASE_URL")),
    secret_key=os.getenv("SECRET_KEY"),
    debug=os.getenv("DEBUG"),
    run=RunConfig()
)
