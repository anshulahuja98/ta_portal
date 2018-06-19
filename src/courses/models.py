from django.db import models
from django.core.validators import RegexValidator
from adminportal.models import FacultyProfile
from django.urls import reverse
from django.db.models.signals import pre_save


class Course(models.Model):
    # Validators
    code = RegexValidator(r'^[A-Z]{2}[0-9]{3}')
    # Models
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=5, validators=[code])
    course_name = models.CharField(max_length=100)
    teaching_assistants = models.ManyToManyField("accounts.TeachingAssistantProfile")
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.course_code

    def get_absolute_url(self):
        return reverse('frontend:course-detail', kwargs={'slug': self.slug})


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.course_code


pre_save.connect(event_pre_save_receiver, sender=Course)
