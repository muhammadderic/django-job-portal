import factory

from application_tracking.models import JobAdvert, JobApplication
from faker import Faker

fake = Faker()


class JobAdvertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JobAdvert

    title = fake.job()
    company_name = fake.company()
    description = fake.sentence()
    skills = "Python, Django"
    deadline = fake.date()


class JobApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JobApplication
    
    name = fake.name()
    portfolio_url = fake.url()
    cv = fake.file_path()
