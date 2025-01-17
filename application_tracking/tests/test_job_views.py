import pytest

from django.test.client import Client
from django.urls import reverse

from .factories import JobAdvertFactory, fake

pytestmark = pytest.mark.django_db


def test_list_adverts(client: Client, user_instance):
    JobAdvertFactory.create_batch(20, created_by=user_instance, deadline=fake.future_date())
    JobAdvertFactory.create_batch(5, created_by=user_instance, deadline=fake.past_date())
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert "job_adverts" in response.context

    paginated_adverts = response.context["job_adverts"]
    assert paginated_adverts.paginator.count == 20
    assert len(paginated_adverts.object_list) == 10