from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from api import api


def custom_generate_unique_id(route: APIRoute):
    if route.include_in_schema:
        return f"{route.tags[0]}-{route.name}"
    else:
        return route.name


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api)


if __name__ == "__main__":
    from uvicorn import run

    run("main:app", reload=True, port=8000)
