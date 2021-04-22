import pytest

from tests import AssertRequest, AssertResponse, assert_request, clean_db
from models import init_db

HEADERS = {"Content-Type": "Application/json"}


# test create_user
ROUTE = "/user/create-user"

CREATE_USER_INPUT = {
    "success1": AssertRequest(HEADERS, {"account": "KJay", "password": "test"}),
    "test_manager": AssertRequest(HEADERS, {"account": "manager", "password": "test"}),
}

CREATE_USER_OUTPUT = {
    "success1": AssertResponse("OK", 200),
    "test_manager": AssertResponse("Bad Request or User already exist", 400),
}


@pytest.mark.parametrize("test_type", CREATE_USER_INPUT.keys())
def test_create_user(test_type):
    clean_db()
    init_db()
    assert_request(
        "POST", ROUTE, CREATE_USER_INPUT[test_type], CREATE_USER_OUTPUT[test_type]
    )
