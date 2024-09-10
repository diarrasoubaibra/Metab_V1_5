from django.db import models

from base.models.helpers.named_date_time_model import NamedDateTimeModel


class SchoolModel(NamedDateTimeModel):
    #app = models.OneToOneField('schools.AppSettingsModel',related_name="school_app_id", on_delete=models.CASCADE)
    app = models.OneToOneField('AppSettingsModel', related_name="school_app_id", on_delete=models.CASCADE)
    url_logo = models.URLField()
