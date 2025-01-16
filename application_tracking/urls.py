from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_advert, name="create_advert"),
    path("<uuid:advert_id>/", views.get_advert, name="job_advert"),
]