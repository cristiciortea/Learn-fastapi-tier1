from fastapi import FastAPI

from app.core import config
from app.db.db_config import db  # instance of DatabaseConnector()

from app.core.base_logger import logging
from app.routes.favs import router

logging.info(f"Application running with the following settings: {config.settings}")


def get_app() -> FastAPI:

    config.get_app_settings.cache_clear()  # use during debuggings
    settings = config.get_app_settings()  # use cached settings

    app_settings = settings.more_settings.dict()
    logging.debug(f"Using app settings: {app_settings}")

    app = FastAPI(**app_settings)

    # On startup, the application is going to connect to the database
    app.add_event_handler("startup", db.initialize_db)

    # Include routes
    app.include_router(router)

    return app


app = get_app()
