from pathlib import Path
from typing import Optional
from pydantic import BaseModel, BaseSettings, Field
from pydantic.tools import lru_cache

from app.core.base_logger import logging

APP_ROOT = Path(__file__).parent.parent


class AppSettings(BaseModel):
    """
    Configuration settings specific to FastAPI.
    Will be accessed as `more settings` in within app.
    """

    title: str = "Favorite Song Application"
    description: str = "This application is a FastAPI Web App that helps you collect all your favorite songs"
    version: str = "0.0.1"
    docs_url: str = "/docs"


class GlobalSettings(BaseSettings):
    """
    Inherits `BaseSettings` from pydantic to provide helpful settings validation and management
    """

    more_settings: AppSettings = AppSettings()

    APP_DIR: Path = APP_ROOT

    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    MONGO_DB: Optional[str] = None
    MONGO_HOST: Optional[str] = None
    MONGO_PORT: Optional[str] = None
    MONGO_USER: Optional[str] = None
    MONGO_PASSWORD: Optional[str] = None
    MONGO_SCHEME: Optional[str] = None

    DB_URI: Optional[str] = None
    FAVORITE_SONG: Optional[str] = None

    class Config:
        env_file = APP_ROOT.parent / ".env"


class DevSettings(GlobalSettings):
    """
    Settings for `dev` environment
    """

    class Config:
        env_prefix: str = "DEV_"


class ProdSettings(GlobalSettings):
    """
    Settings for `prod` environment
    """

    class Config:
        env_prefix: str = "PROD_"


class FactorySettings:
    """
    Callable class that loads Dev or Prod settings based on `ENV_STATE`
    defined in `.env` file
    """

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self, *args, **kwargs):
        if self.env_state == "dev":
            return DevSettings()
        elif self.env_state == "prod":
            return ProdSettings()
        else:
            raise ValueError(f"Invalid env_state: {self.env_state}")


# settings = FactorySettings(GlobalSettings().ENV_STATE)()  # old way


@lru_cache()
def get_app_settings() -> DevSettings | ProdSettings:
    """Returns a cached instance of the settings object."""

    return FactorySettings(GlobalSettings().ENV_STATE)()


settings = get_app_settings()
logging.debug(f"Using following environment: {settings.ENV_STATE}")
