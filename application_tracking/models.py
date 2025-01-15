from django.db import models

from accounts.models import User
from common.models import BaseModel

from .enums import (EmploymentType, ExperienceLevel, LocationType)

class JobAdvert(BaseModel):
    title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    employment_type = models.CharField(
        max_length=50,
        choices=EmploymentType.choices,
        default=EmploymentType.FULL_TIME,
    )
    experience_level = models.CharField(
        max_length=50,
        choices=ExperienceLevel.choices,
        default=ExperienceLevel.ENTRY_LEVEL,
    )
    description = models.TextField()
    job_type = models.CharField(
        max_length=50,
        choices=LocationType.choices,
        default=LocationType.ONSITE,
    )
    location =  models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    deadline = models.DateField()
    skills = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)
    
    def publish_advert(self) -> None:
        self.is_published = True
        self.save(update_fields=["is_published"])