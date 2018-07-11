from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from accounts.models import TeachingAssistantProfile
from adminportal.models import FacultyProfile, TeachingAssistantSupervisorProfile
from django.urls import reverse
from django.db.models.signals import pre_save


class Course(models.Model):
    # Validators
    code = RegexValidator(r'^[A-Z]{2}[0-9]{3}')
    # Models
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=5, validators=[code])
    course_name = models.CharField(max_length=100)
    teaching_assistants = models.ManyToManyField('accounts.TeachingAssistantProfile', blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.course_code

    def get_absolute_url(self):
        return reverse('frontend:past', kwargs={'slug': self.slug})


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.course_code


pre_save.connect(event_pre_save_receiver, sender=Course)


class FeedbackManager(models.Manager):
    def current(self):
        return self.filter(requested_on__month=timezone.now().month)


class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teaching_assistant = models.ForeignKey(TeachingAssistantProfile, on_delete=models.CASCADE, null=True, blank=True)
    teaching_assistant_supervisor = models.ForeignKey(TeachingAssistantSupervisorProfile, blank=True, null=True,
                                                      on_delete=models.SET_NULL)
    requested_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(editable=False, null=True, blank=True)
    changes_requested = models.BooleanField(default=False)
    comments = models.TextField(null=True, blank=True)
    duties_description = models.TextField(null=True, blank=True)

    objects = FeedbackManager()

    def __str__(self):
        return self.course.course_code + ' ' + self.requested_on.strftime(
            '%B') + ' ' + self.teaching_assistant.user.username

    @property
    def get_roll_no(self):
        return self.teaching_assistant.roll_no

    @property
    def is_approved(self):
        return True if (
                self.modified_on and self.comments is not None and
                self.comments != '' and not self.changes_requested
        ) else False


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.teaching_assistant_supervisor:
        instance.teaching_assistant_supervisor = instance.teaching_assistant.teaching_assistant_supervisor
    if not instance._state.adding:
        instance.modified_on = timezone.now()


pre_save.connect(event_pre_save_receiver, sender=Feedback)
