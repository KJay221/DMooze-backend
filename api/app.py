from fastapi import APIRouter, FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
from loguru import logger

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


# Log response status code and body
@APP.middleware("http")
async def log_response(request: Request, call_next):
    response = await call_next(request)
    body = b""
    async for chunk in response.body_iterator:
        body += chunk

    logger.info(f'{response.status_code} {body}')

    return Response(
        content=body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )


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
