from fastapi import FastAPI
from core import config
from core.log.base_logger import logging

logging.info(f"Using the following settings: {config.settings}")


def get_app() -> FastAPI:
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hellow-world"}

    return app


app = get_app()
