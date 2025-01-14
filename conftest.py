import pytest

from django.contrib.auth.hashers import make_password
from django.test.client import Client
from accounts.models import User

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user_instance(db):
    return User.objects.create(
        email="randomabc@gmail.com", password=make_password("abcd")
    )