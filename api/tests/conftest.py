"""
Pytest shared fixtures
"""
import pytest
from api import app


@pytest.fixture(scope='session')
def client():
    client = app.test_client()
    return client
