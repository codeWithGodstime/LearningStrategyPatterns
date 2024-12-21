import factory

from core import models

class ProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Program

    name = factory.Faker("user_name")