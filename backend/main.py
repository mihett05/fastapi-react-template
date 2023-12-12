from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import api
from mongodb import init_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongodb()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api)


if __name__ == "__main__":
    from uvicorn import run

    run("main:app", reload=True, port=8000)
