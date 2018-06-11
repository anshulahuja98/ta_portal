from django.db import models
from django.contrib.auth.models import User


class TeachingAssistantSupervisorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class AdministrativeStaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
