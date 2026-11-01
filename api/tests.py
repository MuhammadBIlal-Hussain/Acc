import pytest
from django.urls import reverse

from accounts.models import Company, Membership, User


@pytest.mark.django_db
def test_health_endpoint_is_public(client):
    response = client.get(reverse("api-health"))
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.django_db
def test_me_endpoint_returns_only_active_memberships(api_client):
    user = User.objects.create_user(username="mobile-user", email="mobile@example.com", password="safe-password-123")
    active = Company.objects.create(name="Mobile Active Co")
    inactive = Company.objects.create(name="Mobile Inactive Co", is_active=False)
    Membership.objects.create(user=user, company=active, role=Membership.Role.ACCOUNTANT)
    Membership.objects.create(user=user, company=inactive, role=Membership.Role.ACCOUNTANT, is_active=False)
    api_client.force_authenticate(user=user)

    response = api_client.get(reverse("api-me"))

    assert response.status_code == 200
    assert [company["name"] for company in response.json()["companies"]] == ["Mobile Active Co"]

