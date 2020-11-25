import datetime
import pytest
from freezegun import freeze_time

from django.shortcuts import reverse

from secure_urls.urls import urlpatterns
from secure_resource.models import SecureElement

pytestmark = pytest.mark.django_db


@pytest.fixture
def secured_url(scope="session"):
    element = SecureElement(
        source_url="https://www.google.com",
        password="12345",
    )
    element.save()
    yield element
    element.delete()


def test_not_expired_redirect_return_200_OK(secured_url, admin_client):
    response = admin_client.get(
        reverse("resources:element-redirect", kwargs={"pk": secured_url.redirect.pk})
    )
    assert response.status_code == 200


@freeze_time("2020-01-01")
def test_expired_redirect_return_410_GONE(secured_url, admin_client):
    expires_at = secured_url.redirect.expires_at
    with freeze_time(str(expires_at)):
        response = admin_client.get(
            reverse(
                "resources:element-redirect", kwargs={"pk": secured_url.redirect.pk}
            )
        )
        assert response.status_code == 410
