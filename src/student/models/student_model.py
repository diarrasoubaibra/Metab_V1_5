from django.db import models

from base.models.person_model import PersonModel


class StudentModel(PersonModel):
    
    matricule = models.CharField(max_length=255)
    phone_number_father = models.CharField(max_length=20)
