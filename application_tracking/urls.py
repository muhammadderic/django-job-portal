from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_advert, name="create_advert"),
    path("my-applications/", views.my_applications, name="my_applications"),
    path("my-jobs/", views.my_jobs, name="my_jobs"),
    path("<uuid:advert_id>/", views.get_advert, name="job_advert"),
    path("<uuid:advert_id>/apply/", views.apply, name="apply_for_job"),
    path("<uuid:advert_id>/update/", views.update_advert, name="update_advert"),
]