from core import configure_logging, config

import uvicorn
from fastapi import FastAPI

configure_logging()

main_app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=config.run.host,
        reload=True
    )
