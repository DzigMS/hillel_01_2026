import os
import uuid

import allure
import pytest

from api_client import DemoQAClient
from model import DemoQaUser, ErrorResponseAccount

USER_EXIST_ERROR = ErrorResponseAccount('1204', 'User exists!')
PASSWORD_ERROR = ErrorResponseAccount('1300', "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.")
REQUIRED_FIELD_ERROR = ErrorResponseAccount('1200', "UserName and Password required.")


def generate_params():
    env = os.getenv('env')

    if env == 'smoke':
        return [(DemoQaUser(username="test_user_1", password="Password1!"), USER_EXIST_ERROR)]
    else:
        return [
            (DemoQaUser(username="test_user_1", password="Password1!"), USER_EXIST_ERROR),
            (DemoQaUser(username="test_user_1", password="Password1"), PASSWORD_ERROR),
            (DemoQaUser(username="", password="Password1!"), REQUIRED_FIELD_ERROR)
        ]
    # return []

@allure.feature("Authorize user")
@pytest.mark.dependency()
def test_is_authorized_registered_user(get_client):
    user = DemoQaUser(username="test_user_1", password="Password1!")

    actual = get_client.is_authorized_user(user)
    assert actual == False

@pytest.fixture
def get_client():
    client = DemoQAClient()
    return client

@allure.description("Test not registered user")
def test_is_authorized_not_registered_user(get_client):
    user = DemoQaUser(username="Test user", password="password")
    actual = get_client.is_authorized_user(user)

    assert actual.code == "1207"
    assert actual.message == "User not found!"


def test_get_unregistered_user(get_client):
    user_id = str(uuid.uuid4())
    user = DemoQaUser(username="test_user", password="password", userId=user_id)

    actual = get_client.get_user(user)

    assert actual.code == "1200"
    assert actual.message == "User not authorized!"

@pytest.mark.dependency(depends=['test_is_authorized_registered_user'])
@pytest.mark.parametrize("user, error", generate_params())
def test_register_registered_user(user, error, get_client):
    # user = DemoQaUser(username="test_user_1", password="Password1!")

    actual = get_client.register_user(user)
    assert actual == error

    assert actual.code == '1204'
    # assert actual.message == 'User exists!'