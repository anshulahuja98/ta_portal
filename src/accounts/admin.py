from django.contrib import admin
from courses.models import Feedback
from .models import TeachingAssistantProfile
from adminportal.views import Pdf


class FeedbackTeachingAssistantInline(admin.StackedInline):
    model = Feedback


@admin.register(TeachingAssistantProfile)
class TeachingAssistantAdmin(admin.ModelAdmin):
    inlines = (FeedbackTeachingAssistantInline,)
    actions = ['pdf_export']

    class Meta:
        model = TeachingAssistantProfile
        fields = '__all__'

    def pdf_export(self, *args, **kwargs):
        Pdf.as_view()


@admin.register(Feedback)
class FeedbackTeachingAssistantAdmin(admin.ModelAdmin):
    list_display = ['get_roll_no', 'course', 'teaching_assistant_supervisor', 'is_approved']
    list_filter = ['teaching_assistant_supervisor', ]

    class Meta:
        model = Feedback
