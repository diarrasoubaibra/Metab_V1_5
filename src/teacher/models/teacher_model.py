from django.db import models

from base.models.person_model import PersonModel


class TeacherModel(PersonModel):
    available = models.BooleanField(default=True)
    specialty = models.CharField(max_length=255)
