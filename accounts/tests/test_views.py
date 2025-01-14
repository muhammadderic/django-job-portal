import pytest

from django.contrib.auth.hashers import check_password
from django.contrib.messages import get_messages
from django.test.client import Client
from django.urls import reverse
from accounts.models import PendingUser

pytestmark = pytest.mark.django_db

def test_register_user(client: Client):
    url = reverse("register")
    request_data = {"email": "abc@gmail.com", "password": "12345678"}
    response = client.post(url, request_data)
    assert response.status_code == 200
    pending_user = PendingUser.objects.filter(email=request_data["email"]).first()
    assert pending_user
    assert check_password(request_data["password"], pending_user.password)

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert messages[0].level_tag == "success"
    assert "Verification code sent to" in str(messages[0])