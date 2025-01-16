from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobAdvertForm, JobApplicationForm
from .models import JobAdvert


def create_advert(request: HttpRequest):
    form = JobAdvertForm(request.POST or None)

    if form.is_valid():
        instance: JobAdvert = form.save(commit=False)
        instance.created_by = request.user
        instance.save()

        messages.success(request, "Advert created. You can now receive applications.")
        return redirect(instance.get_absolute_url())

    context = {
        "job_advert_form":form,
        "title": "Create a new advert",
        "btn_text": "Create advert"
    }

    return render(request, "create_advert.html", context)


def get_advert(request: HttpRequest, advert_id):
    form = JobApplicationForm()
    job_advert = get_object_or_404(JobAdvert, pk=advert_id)
    context = {
        "job_advert": job_advert,
        "application_form": form,
    }

    return render(request, "advert.html", context)