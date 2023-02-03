from hello_world import __version__
import pytest


@pytest.fixture
def client():
    from hello_world.app import app

    with app.test_client() as client:
        yield client


def test_version():
    assert __version__ == '0.1.0'


def test_hello_world(client):
    response = client.open("/", method="GET")
    assert response.status_code == 200
    assert response.text == "Hello World!"