import pytest

from django.contrib.messages import get_messages
from django.test.client import Client
from django.urls import reverse

from application_tracking.models import JobAdvert

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


def test_create_advert(authenticate_user_client):
    client, user = authenticate_user_client
    url = reverse("create_advert")

    request_data = {
        "title": "Title",
        "company_name": "Deric Inc",
        "employment_type": "Full Time",
        "experience_level" : "Senior",
        "job_type": "Remote",
        "deadline": "2025-05-22",
        "skills": "Python, Django",
        "description": "Sample"
    }

    response = client.post(url, request_data)
    assert response.status_code == 302

    assert JobAdvert.objects.count() == 1
    assert JobAdvert.objects.filter(created_by=user).count() == 1

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert messages[0].level_tag == "success"