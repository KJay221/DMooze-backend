from endpoints.classes import Resource

from .put import put

IMAGE = [
    Resource(
        "PUT",
        "/image",
        put,
        "Used for upload image",
        "Upload image",
    ),
]
