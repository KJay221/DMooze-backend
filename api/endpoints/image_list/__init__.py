from endpoints.classes import Resource

from .post import post

IMAGE = [
    Resource(
        "POST",
        "/image",
        post,
        "Used for upload image",
        "Upload image",
    ),
]
