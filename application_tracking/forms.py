from django.forms import ModelForm
from .models import JobAdvert
from django import forms

class JobAdvertForm(ModelForm):
    class Meta:
        model = JobAdvert
        fields = [
            "title",
            "company_name",
            "employment_type",
            "experience_level",
            "job_type",
            "location",
            "description",
            "skills",
            "is_published",
            "deadline"
        ]

        widgets = {
            "title": forms.TextInput(attrs={"placeholder":"Job title", "class":"form-control"}),
            "description": forms.Textarea(attrs={"placeholder":"Description", "class":"form-control"}),
            "company_name": forms.TextInput(attrs={"placeholder":"Company name", "class":"form-control"}),
            "employment_type": forms.Select(attrs={"class":"form-control"}),
            "experience_level": forms.Select(attrs={"class":"form-control"}),
            "job_type": forms.Select(attrs={"class":"form-control"}),
            "location": forms.TextInput(attrs={"placeholder":"Optional", "class":"form-control"}),
            "deadline": forms.DateInput(attrs={"placeholder":"Date", "class":"form-control", "type":"date"}),
            "skills": forms.TextInput(attrs={"placeholder":"Comma separated skills", "class":"form-control"}),
        }