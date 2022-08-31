from app.crud.favs import get_fav_song, create_fav_song
from app.models.favs import FavoriteSongCreate

from fastapi.responses import HTMLResponse, JSONResponse

from fastapi import APIRouter

router = APIRouter()


@router.get("/song")
async def song_retrieval(song: str):
    return await get_fav_song(song)


@router.post("/add_song")
async def song_creation(song_entry: FavoriteSongCreate):
    return await create_fav_song(**song_entry.dict())


# My default routes
@router.get("/")
async def root():
    return {"message": "Hellow-world"}


@router.get(
    "/offcell", response_class=JSONResponse
)  # JSONResponse is redundant here because its the default option
async def proceed_to_memory():
    return {"converts": "to json"}


@router.get("/walters", response_class=HTMLResponse)
async def weather_balloon():
    return """
    <html>
        <head>Singing</head>
        <body>
        Get me down
        Get me down
        </body>
    </html>
    """
