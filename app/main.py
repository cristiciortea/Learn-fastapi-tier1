from fastapi import FastAPI


def get_app() -> FastAPI:
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hellow-world"}

    return app


app = get_app()
