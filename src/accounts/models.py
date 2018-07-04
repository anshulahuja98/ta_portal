from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save
from adminportal.models import TeachingAssistantSupervisorProfile


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
    roll_no = models.CharField(max_length=8, validators=[roll], blank=True)
    program = models.CharField(max_length=1, choices=PROGRAMS)
    phone = models.CharField(max_length=10, validators=[contact])
    slug = models.SlugField(blank=True)
    teaching_assistant_supervisor = models.ForeignKey(TeachingAssistantSupervisorProfile, null=True, blank=True,
                                                      on_delete=models.SET_NULL)
    alternate_pno = models.CharField(max_length=10, validators=[contact], blank=True)
    research_area = models.CharField(max_length=100, blank=True)
    ug_course = models.CharField(max_length=50, null=True, blank=True)
    pg_course = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.roll_no + '(' + self.user.get_full_name() + ')'

    def get_absolute_url(self):
        return "/details/"


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug or not instance.roll_no:
        instance.slug = instance.user.username
        instance.roll_no = instance.user.username


pre_save.connect(event_pre_save_receiver, sender=TeachingAssistantProfile)
