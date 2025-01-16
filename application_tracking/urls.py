from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_advert, name="create_advert"),
]