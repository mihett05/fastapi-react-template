from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from sqlalchemy.exc import IntegrityError

from api import api
from auth.exceptions import InvalidCredentials
from core.exceptions import EntityNotFound, PermissionDenied


def custom_generate_unique_id(route: APIRoute):
    if route.include_in_schema:
        return f"{route.tags[0]}-{route.name}"
    return route.name


app = FastAPI(docs_url="/docs", generate_unique_id_function=custom_generate_unique_id)


@app.exception_handler(IntegrityError)
async def invalid_data_was_provide_exception_handler(_: Request, exc: EntityNotFound):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": exc.args[0] if exc.args else "Invalid data was provide"},
    )


@app.exception_handler(EntityNotFound)
async def entity_not_found_exception_handler(_: Request, exc: EntityNotFound):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": exc.args[0] if exc.args else "Entity not found"},
    )


@app.exception_handler(PermissionDenied)
async def permission_denied_exception_handler(_: Request, exc: EntityNotFound):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={"message": exc.args[0] if exc.args else "Permission denied"},
    )


@app.exception_handler(InvalidCredentials)
async def invalid_credentials_exception_handler(_: Request, exc: InvalidCredentials):
    return JSONResponse(
        status_code=status.HTTP_401_BAD_REQUEST,
        content={
            "message": exc.args[0] if exc.args else "Invalid credentials were provided"
        },
    )


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

    run("main:app", reload=True, port=5000, host="0.0.0.0")
