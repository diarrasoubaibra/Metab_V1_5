from django.db import models

class RoleUserModel(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role
