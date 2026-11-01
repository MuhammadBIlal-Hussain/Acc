import pytest
from django.urls import reverse

from .models import Company, Membership, User


@pytest.mark.django_db
def test_anonymous_user_is_redirected_to_login(client):
    response = client.get(reverse("dashboard"))
    assert response.status_code == 302
    assert reverse("login") in response["Location"]


@pytest.mark.django_db
def test_dashboard_only_displays_active_companies(client):
    user = User.objects.create_user(username="aisha", email="aisha@example.com", password="safe-password-123")
    active = Company.objects.create(name="Active Trading Co")
    inactive = Company.objects.create(name="Closed Trading Co", is_active=False)
    Membership.objects.create(user=user, company=active, role=Membership.Role.OWNER)
    Membership.objects.create(user=user, company=inactive, role=Membership.Role.OWNER, is_active=False)
    client.force_login(user)

    response = client.get(reverse("dashboard"))

    assert response.status_code == 200
    assert b"Active Trading Co" in response.content
    assert b"Closed Trading Co" not in response.content


@pytest.mark.django_db
def test_membership_is_unique_per_user_and_company():
    user = User.objects.create_user(username="umar", email="umar@example.com", password="safe-password-123")
    company = Company.objects.create(name="Unique Co")
    Membership.objects.create(user=user, company=company)

    with pytest.raises(Exception):
        Membership.objects.create(user=user, company=company)
