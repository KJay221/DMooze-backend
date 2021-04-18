from fastapi import APIRouter, FastAPI

from config import Config
from endpoints import RESOURCES
from models import init_db

APP = FastAPI(
    version=Config.VERSION,
    title=Config.APP_TITLE,
    description=Config.APP_DESCRIPTION,
    openapi_url=Config.OPENAPI_URL
)
API_ROUTER = APIRouter()


# Startup event
@APP.on_event("startup")
async def startup_event():
    init_db()


# Add routes from resources
for resource in RESOURCES:
    API_ROUTER.add_api_route(
        resource.route,
        resource.endpoint,
        description=resource.description,
        summary=resource.summary,
        methods=[resource.method],
        responses=resource.doc,
    )

APP.include_router(API_ROUTER)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(APP, host="127.0.0.1", port=8000)
