from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
