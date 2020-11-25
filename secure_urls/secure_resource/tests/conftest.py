import pytest

# from django.conf import settings
from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def athenticated_client():
    client = APIClient()
    client.login(username="admin", password="admin")
    return client
