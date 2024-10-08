from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    # Abstract user already requires username and password, so we just have to add the extra fields that we want for our users
    email = models.CharField(max_length=50, unique=True, validators=[
            RegexValidator(
                # validator regex for email
                regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message="Enter a valid email",
                code="invalid_registration",
            ),
        ],)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)