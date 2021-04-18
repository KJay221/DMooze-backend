from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

# Document for generating custom response
# References: https://fastapi.tiangolo.com/advanced/additional-responses
DOC = {
    200: {
        "description": "API response successfully",
        "content": {"OK"},
    }
}


def create_user():
    return PlainTextResponse("OK", 200)
