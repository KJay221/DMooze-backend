from endpoints.classes import Resource

from .post import post

WITHDRAWAL = [
    Resource(
        "POST",
        "/withdrawal",
        post,
        "Used for upload withdrawal record",
        "Upload withdrawal record",
    ),
]
