from django.db import models

from base.models.helpers.date_time_model import DateTimeModel

from user.models import gender_model

class PersonModel(DateTimeModel):
    GENDER_CHOICES = (
        ('M','MALE'),
        ('F','FEMALE'),
        ('O','OTHER'),
     )
    
    user = models.OneToOneField('user.UserModel', on_delete=models.CASCADE) 
    address = models.OneToOneField('base.AddressModel', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=20)
    url_picture = models.URLField()
    gender = models.CharField(max_length=10, choices=gender_model.Gender.choices)

    class Meta:
        abstract = True