from typing import Optional
from app.models.favs import FavoriteSongDB, FavoriteSongCreate


async def get_fav_song(song: str) -> dict:
    """Get a favorite song by song title."""
    fav_song = await FavoriteSongDB.find_one(  # Beanie ODM
        FavoriteSongDB.song_title == song
    )

    if not fav_song:
        return {"message": f"{song} not found."}
    return fav_song.dict()


async def create_fav_song(
    song_title: str,
    artist: str,
    description: Optional[str] = None,
) -> FavoriteSongCreate:
    """Create a new favorite song."""
    fav_song = FavoriteSongCreate(
        song_title=song_title,
        artist=artist,
        description=description,
    )
    await FavoriteSongDB(**fav_song.dict()).save()  # Beanie
    return fav_song
