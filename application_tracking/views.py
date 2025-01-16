from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .forms import JobAdvertForm
from .models import JobAdvert


def create_advert(request: HttpRequest):
    form = JobAdvertForm(request.POST or None)

    if form.is_valid():
        instance: JobAdvert = form.save(commit=False)
        instance.created_by = request.user
        instance.save()

        messages.success(request, "Advert created. You can now receive applications.")
        return

    context = {
        "job_advert_form":form,
        "title": "Create a new advert",
        "btn_text": "Create advert"
    }

    return render(request, "create_advert.html", context)
