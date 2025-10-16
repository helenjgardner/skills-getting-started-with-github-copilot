import sys
import os
import pytest

# ensure src is importable
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

from fastapi.testclient import TestClient
from app import app


@pytest.fixture(scope='function')
def client():
    return TestClient(app)
