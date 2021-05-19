import glob
import os

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import Config
from endpoints import RESOURCES
from models import init_db

APP = FastAPI(
    version=Config.VERSION,
    title=Config.APP_TITLE,
    description=Config.APP_DESCRIPTION,
    openapi_url=Config.OPENAPI_URL,
)

FILES = glob.glob("./static/img/*")
for img_file in FILES:
    os.remove(img_file)
APP.mount("/static", StaticFiles(directory="static"), name="static")

API_ROUTER = APIRouter()


# Startup event
@APP.on_event("startup")
async def startup_event():
    init_db()


APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add routes from resources
for resource in RESOURCES:
    API_ROUTER.add_api_route(
        resource.route,
        resource.endpoint,
        description=resource.description,
        summary=resource.summary,
        methods=[resource.method],
    )

APP.include_router(API_ROUTER)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(APP, host=Config.HOST, port=Config.PORT)
