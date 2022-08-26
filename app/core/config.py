from pathlib import Path

from typing import Optional

from pydantic import BaseModel, BaseSettings, Field

APP_ROOT = Path(__file__).parent.parent


class AppSettings(BaseModel):
    """
    Configuration settings specific to FastAPI.
    Will be accessed as `more settings` in within app.
    """

    ...


class GlobalSettings(BaseSettings):
    """
    Inherits `BaseSettings` from pydantic to provide helpful settings validation and management
    """

    APP_DIR: Path = APP_ROOT

    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    DB_URI: Optional[str] = None
    FAVORITE_SONG: Optional[str] = None

    class Config:
        env_file = APP_ROOT.parent / ".env"


print(GlobalSettings())


class DevSettings(GlobalSettings):
    """
    Settings for `dev` environment
    """

    ...


class ProdSettings(GlobalSettings):
    """
    Settings for `prod` environment
    """

    ...


class FactorySettings:
    """
    Callable class that loads Dev or Prod settings based on `ENV_STATE`
    defined in `.env` file
    """
