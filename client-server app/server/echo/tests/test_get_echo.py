import pytest
from datetime import datetime
from echo.controllers import get_echo


@pytest.fixture
def action_fixture():
    print('connect to db')
    return 'echo'


@pytest.fixture
def time_fixture():
    return datetime.now().timestamp()


@pytest.fixture
def data_fixture():
    return 'some data'


@pytest.fixture
def request_fixture(action_fixture, time_fixture, data_fixture):
    return {
        'action': action_fixture,
        'time': time_fixture,
        'data': data_fixture
    }


@pytest.fixture
def response_fixture(action_fixture, time_fixture, data_fixture):
    return {
        'action': action_fixture,
        'time': time_fixture,
        'user': None,
        'data': data_fixture,
        'code': 200
    }


def test_get_echo(request_fixture, response_fixture):
    """
    action_name = 'echo'
    data = 'some data'

    request = {
        'action': action_name,
        'time': datetime.now().timestamp(),
        'data': data
    }

    expected_response = {
        'action': action_name,
        'time': datetime.now().timestamp(),
        'user': None,
        'data': data,
        'code': 200
    }
    """

    response = get_echo(request_fixture)

    assert response_fixture.get('code') == response.get('code')
    # assert expected_response.get('code') == response.get('code')
