from fastapi import Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from auth.exceptions import InvalidCredentials
from backend import app
from core.exceptions import EntityNotFound, PermissionDenied


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
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "message": exc.args[0] if exc.args else "Invalid credentials were provided"
        },
    )
