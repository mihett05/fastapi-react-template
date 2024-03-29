from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import api
from mongodb import init_mongodb


@asynccontextmanager
async def lifespan(*args):
    await init_mongodb()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    from uvicorn import run

    run("main:app", reload=True, port=8000)
