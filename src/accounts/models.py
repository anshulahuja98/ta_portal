from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from courses.models import Course


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

    def __str__(self):
        return self.rollno + '(' + self.user.get_full_name() + ')'


class FeedbackTeachingAssistant(models.Model):
    MONTHES = (
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
    )
    approve = models.BooleanField(default=False)
    comments = models.TextField(null=True, blank=True)
    month = models.CharField(max_length=2, choices=MONTHES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ta = models.ForeignKey(TeachingAssistantProfile, on_delete=models.CASCADE)
