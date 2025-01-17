import factory

from application_tracking.models import JobAdvert
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