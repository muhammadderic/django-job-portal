from django.db import models

class EmploymentType(models.TextChoices):
    FULL_TIME = "Full Time", "Full Time"
    PART_TIME = "Part Time", "Part Time"
    CONTRACT = "Contract", "Contract"


class ExperienceLevel(models.TextChoices):
    ENTRY_LEVEL = "Entry Level", "Entry Level"
    MID_LEVEL = "Mid Level", "Mid Level"
    SENIOR = "Senior", "Senior"


class LocationType(models.TextChoices):
    ONSITE = "Onsite", "Onsite"
    HYBRID = "Hybrid", "Hybrid"
    REMOTE = "Remote", "Remote"


class ApplicationStatus(models.TextChoices):
    APPLIED = ("APPLIED", "APPLIED")
    REJECTED = ("REJECTED", "REJECTED")
    INTERVIEW = ("INTERVIEW", "INTERVIEW")