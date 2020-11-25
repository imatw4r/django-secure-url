import pytest

pytestmark = pytest.mark.django_db


def test_endpoint(authenticated_client):
    assert False
