from backend import app  # noqa
import backend.add_exception_handlers  # noqa

if __name__ == "__main__":
    from uvicorn import run

    run("main:app", reload=True, port=5000, host="0.0.0.0")
