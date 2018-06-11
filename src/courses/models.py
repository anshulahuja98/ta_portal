from django.db import models
from django.core.validators import RegexValidator
from accounts.models import TeachingAssistantProfile
from adminportal.models import FacultyProfile


class Course(models.Model):
    # Validators
    code = RegexValidator(r'^[A-Z]{2}[0-9]{3}')
    # Models
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=5, validators=[code])
    course_name = models.CharField(max_length=100)
    teaching_assistants = models.ManyToManyField(TeachingAssistantProfile)
