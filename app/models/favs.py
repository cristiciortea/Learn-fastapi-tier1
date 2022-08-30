from typing import Optional

from beanie import Document
from pydantic import BaseModel


class FavoriteSong(BaseModel):
    song_title: str
    artist: str
    description: Optional[str] = None


class FavoriteSongCreate(FavoriteSong):
    pass


class FavoriteSongDB(FavoriteSong, Document):
    pass

    class Collection:
        name: str = "Favorite_songs"
