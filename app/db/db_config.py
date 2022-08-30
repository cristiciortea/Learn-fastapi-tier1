from typing import Optional

from app.core.config import settings
from pydantic import AnyUrl, BaseSettings, validator

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.favs import FavoriteSongDB


class DatabaseConnector(BaseSettings):
    """Load database settings and build valid URI."""

    MONGO_DB_URI: Optional[AnyUrl] = None

    @validator("MONGO_DB_URI", pre=True, check_fields=False)
    def uri_is_valid(cls, v):
        if isinstance(cls, AnyUrl):
            return v

        if settings.MONGO_HOST in ("localhost", "127.0.0.1"):
            try:
                return AnyUrl.build(
                    host=settings.MONGO_HOST,
                    port=settings.MONGO_PORT,
                    user=settings.MONGO_USER,
                    password=settings.MONGO_PASSWORD,
                    path=f"/{settings.MONGO_DB}",
                    scheme=settings.MONGO_SCHEME,
                    query="retryWrites=true&w=majority",
                )  # build URI string for local mongodb
            except Exception:
                raise AttributeError(v)

        try:
            return AnyUrl.build(
                host=settings.MONGO_HOST,
                user=settings.MONGO_USER,
                password=settings.MONGO_PASSWORD,
                path=f"/{settings.MONGO_DB}",
                scheme=settings.MONGO_SCHEME,
                query="retryWrites=true&w=majority",
            )  # build URI string for local mongodb  # otherwise, try to build URI with current settings
        except Exception:
            raise AttributeError(v)

    async def initialize_db(self) -> None:
        """
        Start db client with Beanie and load document models.
        """
        # Using motor to instatiate the db client
        client = AsyncIOMotorClient(self.MONGO_DB_URI)
        models = [FavoriteSongDB]

        try:
            await init_beanie(
                database=client[settings.MONGO_DB], document_models=models
            )
        except Exception:
            raise ConnectionError("Database initialization failed.")


db = DatabaseConnector()  # import this instance in main.py
