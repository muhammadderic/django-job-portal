from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from accounts.models import User

from .forms import JobAdvertForm, JobApplicationForm
from .models import JobAdvert, JobApplication


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


def list_adverts(request: HttpRequest):
    active_jobs = JobAdvert.objects.active()

    paginator = Paginator(active_jobs, 10)
    requested_page = request.GET.get("page")
    paginated_adverts = paginator.get_page(requested_page)
   
    context = {
        "job_adverts": paginated_adverts
    }
    return render(request, "home.html", context)


def get_advert(request: HttpRequest, advert_id):
    form = JobApplicationForm()
    job_advert = get_object_or_404(JobAdvert, pk=advert_id)
    context = {
        "job_advert": job_advert,
        "application_form": form,
    }

    return render(request, "advert.html", context)


def update_advert(request: HttpRequest, advert_id):
    advert: JobAdvert = get_object_or_404(JobAdvert, pk=advert_id)
    if request.user != advert.created_by:
        return HttpResponseForbidden("You can only update an advert created by you.")
    
    form = JobAdvertForm(request.POST or None, instance=advert)
    if form.is_valid():
        instance: JobAdvert = form.save(commit=False)
        instance.save()
        messages.success(request, "Advert updated successfully.")
        return redirect(instance.get_absolute_url())
    
    context = {
        "job_advert_form": form,
        "btn_text": "Update advert"
    }
    return render(request, "create_advert.html", context)


def delete_advert(request: HttpRequest, advert_id):
    advert: JobAdvert = get_object_or_404(JobAdvert, pk=advert_id)
    if request.user != advert.created_by:
        return HttpResponseForbidden("You can only update an advert created by you.")
    
    advert.delete()
    messages.success(request, "Advert deleted successfully.")
    return redirect("my_jobs")


def apply(request: HttpRequest, advert_id):
    advert = get_object_or_404(JobAdvert, pk=advert_id)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Prevent duplicate applications for the same email
            email = form.cleaned_data["email"]
            if advert.applications.filter(email__iexact=email).exists():
                messages.error(request, "You have already applied for this position")
                return redirect("job_advert", advert_id=advert_id)
            
            # Save the new application
            application: JobApplication = form.save(commit=False)
            application.job_advert = advert
            application.save()
            messages.success(request, "Application submitted successfully.")
            return redirect("job_advert", advert_id=advert_id)

    else:
        form = JobApplicationForm()
    
    context = {
        "job_advert": advert,
        "application_form": form
    }
    return render(request, "advert.html", context)


def my_applications(request: HttpRequest):
    user: User = request.user
    applications = JobApplication.objects.filter(email=user.email)
    paginator = Paginator(applications, 10)

    requested_page = request.GET.get("page")
    paginated_applications = paginator.get_page(requested_page)

    context = {
        "my_applications": paginated_applications
    }

    return render(request, "my_applications.html", context)


def my_jobs(request: HttpRequest):
    user: User = request.user
    jobs = JobAdvert.objects.filter(created_by=user)
    paginator = Paginator(jobs, 10)
    requested_page = request.GET.get("page")
    paginated_jobs = paginator.get_page(requested_page)

    context = {
        "my_jobs": paginated_jobs,
        "current_date": timezone.now().date()
    }

    return render(request, "my_jobs.html",  context)