import pytest

from tests import AssertRequest, AssertResponse, assert_request, clean_db
from models import init_db

ROUTE = "/proposal/create_proposal"

HEADERS = {"Content-Type": "Application/json"}

POST_INPUT = {
    "success_input1": AssertRequest(
        HEADERS,
        {
            "owner_addr": "0xea674fdde714fd979de3edf0f56aa97154545464",
            "target_price": 1123123232,
            "project_description": "GOOD???",
            "start_time": "2021-04-22T13:49",
            "end_time": "2021-04-22T13:49",
            "project_name": "Jay project",
            "representative": "Jay",
            "email": "KKKKKKKK@gami;.com",
            "phone": "0922223445",
        },
    ),
    "success_input2": AssertRequest(
        HEADERS,
        {
            "owner_addr": "0xfdd79de3edea674f0f56aa971e714fd96b898ec8",
            "target_price": 132323232,
            "project_description": "GOOD???",
            "start_time": "2021-04-22T13:49",
            "end_time": "2021-04-22T13:49",
            "project_name": "Jay project",
            "representative": "Jay",
            "email": "KKKKKKKK@gami;.com",
            "phone": "0922223445",
        },
    ),
    "success_input3": AssertRequest(
        HEADERS,
        {
            "owner_addr": "0xe3edf0f6da979de56aa9774fdde714f16b898ec8",
            "target_price": 1223232122,
            "project_description": "GOOD",
            "start_time": "2021-04-01T13:49",
            "end_time": "2021-04-22T13:49",
            "project_name": "Jay2 project",
            "representative": "Jay2",
            "email": "KK478797234@gami;.com",
            "phone": "0922342245",
        },
    ),
    "success_input4": AssertRequest(
        HEADERS,
        {
            "owner_addr": "0xea674fddf0f56aa9716b8de714fd979de3e98ec8",
            "target_price": 1222222,
            "project_description": "GOOD",
            "start_time": "2021-04-10T23:30",
            "end_time": "2021-04-23T13:49",
            "project_name": "Jay1 project",
            "representative": "Jay1",
            "email": "HJHI23123HIKKK@gami.com",
            "phone": "0970333333",
        },
    ),
    "fail": AssertRequest(
        HEADERS,
        {
            "owner_addr": "0xea67df0f56aa9716b8dde714fd94f79de3e98ec8",
            "target_price": 1000,
            "project_description": "GOOD??",
            "start_time": "2021-04-10T13:49:29",
            "end_time": "2021-04-22T13:49",
            "project_name": "Jay project",
            "representative": "Jay",
            "email": "KKKKKKKK@gami.com",
            "phone": "090000000000000000000000000000000000",
        },
    ),
}

POST_OUTPUT = {
    "success_input1": AssertResponse("successfully create", 200),
    "success_input2": AssertResponse("successfully create", 200),
    "success_input3": AssertResponse("successfully create", 200),
    "success_input4": AssertResponse("successfully create", 200),
    "fail": AssertResponse("Bad Request(check input data size and type)", 400),
}

clean_db()
@pytest.mark.parametrize("test_type", POST_INPUT.keys())
def test_post(test_type):
    init_db()
    assert_request("POST", ROUTE, POST_INPUT[test_type], POST_OUTPUT[test_type])
