import pytest
from starlette.testclient import TestClient


@pytest.fixture
def client():
    from app.main import app

    return TestClient(app)
