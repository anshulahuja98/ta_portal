from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from courses.models import Course
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
    rollno = models.CharField(max_length=8, validators=[roll], blank=True)
    program = models.CharField(max_length=1, choices=PROGRAMS)
    phone = models.CharField(max_length=10, validators=[contact])
    slug = models.SlugField(blank=True)
    teaching_assistant_supervisor = models.ForeignKey(TeachingAssistantSupervisorProfile, null=True, blank=True,
                                                      on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.rollno + '(' + self.user.get_full_name() + ')'


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug or not instance.rollno:
        instance.slug = instance.user.username
        instance.rollno = instance.user.username


pre_save.connect(event_pre_save_receiver, sender=TeachingAssistantProfile)


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
    comments = models.TextField(null=True, blank=True, )
    month = models.CharField(max_length=2, choices=MONTHES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teaching_assistant = models.ForeignKey(TeachingAssistantProfile, on_delete=models.CASCADE)
    teaching_assistant_supervisor = models.ForeignKey(TeachingAssistantSupervisorProfile, blank=True, null=True,
                                                      on_delete=models.DO_NOTHING)

    @property
    def get_rollno(self):
        return self.teaching_assistant.rollno


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.teaching_assistant_supervisor:
        instance.teaching_assistant_supervisor = instance.ta.teaching_assistant_supervisor


pre_save.connect(event_pre_save_receiver, sender=FeedbackTeachingAssistant)
