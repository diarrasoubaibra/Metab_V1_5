from django.db import models

from base.models.helpers.date_time_model import DateTimeModel




class AbsenceModel(DateTimeModel):
    student = models.ForeignKey('student.StudentModel',related_name='absence_student_ids', on_delete=models.CASCADE)
    absence_date = models.DateField()
    absence_number = models.IntegerField()