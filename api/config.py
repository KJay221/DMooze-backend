import os


class Config:
    """Service configurations"""

    APP_TITLE = os.environ.get("APP_TITLE", "FastAPI template")
    APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION", "A template for FastAPI.")
    VERSION = os.environ.get("VERSION", "0.0.0")
    OPENAPI_URL = os.environ.get("OPENAPI_URL", "/openapi.json")

    DB_URL = os.environ.get(
        "DB_URL", "postgresql://postgres:password@localhost:5432/database"
    )

    HOST = os.environ.get("HOST", "0.0.0.0")
    PORT = int(os.environ.get("PORT", "8000"))

    FAKE_DATA_INSERT = os.environ.get("FAKE_DATA_INSERT", "false")

    IMG_URL = os.environ.get("IMG_URL", "http://127.0.0.1:8000/static/")
