from django.contrib import admin
from .models import TeachingAssistantProfile, FeedbackTeachingAssistant
from adminportal.views import Pdf


class FeedbackTeachingAssistantInline(admin.StackedInline):
    model = FeedbackTeachingAssistant


@admin.register(TeachingAssistantProfile)
class TeachingAssistantAdmin(admin.ModelAdmin):
    inlines = (FeedbackTeachingAssistantInline,)
    actions = ['pdf_export']

    class Meta:
        model = TeachingAssistantProfile
        fields = '__all__'

    def pdf_export(self, *args, **kwargs):
        Pdf.as_view()


@admin.register(FeedbackTeachingAssistant)
class FeedbackTeachingAssistantAdmin(admin.ModelAdmin):
    list_display = ['get_rollno', 'course', 'teaching_assistant_supervisor', 'approve']
    list_filter = ['teaching_assistant_supervisor', ]

    class Meta:
        model = FeedbackTeachingAssistant
