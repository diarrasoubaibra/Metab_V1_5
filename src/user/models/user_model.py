from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


from django.contrib.auth.models import BaseUserManager

from user.models.role_user_model import RoleUserModel

class UserManager(BaseUserManager):
    def get_by_natural_key(self, pseudo):
        return self.get(pseudo=pseudo)
    
    def create_user(self, pseudo, password=None, **extra_fields):
        """
        Crée et sauvegarde un utilisateur normal avec le pseudo et le mot de passe donnés.
        """
        if not pseudo:
            raise ValueError('Le pseudo doit être renseigné')
        user = self.model(pseudo=pseudo, **extra_fields)
        user.set_password(password)  # Hash le mot de passe
        user.save(using=self._db)
        return user

    def create_superuser(self, pseudo, password=None, **extra_fields):
        """
        Crée et sauvegarde un super utilisateur.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        # Assigner un rôle par défaut pour le super utilisateur (exemple: "Super Admin")
        super_admin_role, created = RoleUserModel.objects.get_or_create(role="Super Admin")
        extra_fields.setdefault('role', super_admin_role)

        return self.create_user(pseudo, password, **extra_fields)


class UserModel(AbstractBaseUser, PermissionsMixin, DateTimeModel):
    school = models.ForeignKey('school.SchoolModel', on_delete=models.CASCADE,  null=True, blank=True)
    role = models.ForeignKey('user.RoleUserModel', on_delete=models.CASCADE, null=True, blank=True)
    pseudo = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Ajout des related_name uniques pour éviter les conflits avec 'auth.User'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Un nom unique
        blank=True,
        help_text="The groups this user belongs to."
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Un autre nom unique
        blank=True,
        help_text="Specific permissions for this user."
    )

    USERNAME_FIELD = 'pseudo'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.pseudo

