from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class TeachingAssistantProfile(models.Model):
    # Choices
    PROGRAMS = (
        ('1', 'M.Tech'),
        ('2', 'PhD'),
    )
    # Validators
    roll = RegexValidator(r'^[BMP][0-9]{2}[A-Z]{2}[0-9]{3}')
    contact = RegexValidator(r'^[6-9][0-9]{9}')
    # Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollno = models.CharField(max_length=8, validators=[roll])
    program = models.CharField(max_length=1, choices=PROGRAMS)
    phone = models.CharField(max_length=10, validators=[contact])
