from endpoints.classes import Resource

from .create_user import DOC as create_user_doc
from .create_user import create_user

USER = [
    Resource(
        "POST",
        "/user/create-user",
        create_user,
        "Used for create user",
        "Create user",
        create_user_doc,
    )
]
