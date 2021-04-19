from endpoints.classes import Resource

from .create_user import create_user
from .user_login import user_login

USER = [
    Resource(
        "POST", "/user/create-user", create_user, "Used for create user", "Create user"
    ),
    Resource(
        "POST", "/user/user_login", user_login, "Used for user get token", "User login"
    ),
]
