from endpoints.classes import Resource

from .delete import delete
from .get import get
from .post import post
from .put import put

FRUIT = [
    Resource("GET", "/fruit", get, "Retrieve a fruit", "GET fruit"),
    Resource("PUT", "/fruit", put, "Update a fruit", "UPDATE fruit"),
    Resource("POST", "/fruit", post, "Create a fruit", "CREATE fruit"),
    Resource("DELETE", "/fruit", delete, "Delete a fruit", "DELETE fruit"),
]
