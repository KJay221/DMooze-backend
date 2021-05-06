from endpoints.classes import Resource

from .get import get
from .post import post
from .put import put

PROPOSAL = [
    Resource(
        "POST",
        "/proposal",
        post,
        "Used for create id",
        "Create id and return id",
    ),
    Resource(
        "PUT",
        "/proposal",
        put,
        "Used for update proposal info",
        "Update proposal info",
    ),
    Resource(
        "GET",
        "/proposal",
        get,
        "Used for get proposal info",
        "Get proposal info",
    ),
]
