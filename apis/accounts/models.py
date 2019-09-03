from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    ROLES = (("0", "Super"), ("1", "Admin"), ("2", "Reporter"), ("3", "Guest"))
    role = models.CharField(choices=ROLES, default="3", max_length=1)
    email = models.EmailField(_('email address'), unique=True)
    # is_delete = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "role", "first_name", "last_name")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    dob = models.DateField()
    address = models.CharField(max_length=50)
    
