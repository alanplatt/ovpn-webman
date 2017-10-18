from ovpnWebman import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client

def test_home(client):
    rv = client.get('/')
    assert b"Generate personal VPN certificate" in rv.data
