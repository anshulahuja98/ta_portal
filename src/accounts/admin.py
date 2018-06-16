from django.contrib import admin
from .models import TeachingAssistantProfile, FeedbackTeachingAssistant
from adminportal.models import TeachingAssistantSupervisorProfile


class FeedbackTeachingAssistantInline(admin.StackedInline):
    model = FeedbackTeachingAssistant


@admin.register(TeachingAssistantProfile)
class TeachingAssistantAdmin(admin.ModelAdmin):
    inlines = (FeedbackTeachingAssistantInline,)
    list_display = ('rollno',)

    class Meta:
        model = TeachingAssistantProfile
        fields = '__all__'


@admin.register(FeedbackTeachingAssistant)
class FeedbackTeachingAssistantAdmin(admin.ModelAdmin):
    list_display = ['get_rollno', 'course', 'ta_sup', 'approve']
    list_filter = ['ta_sup',]

    class Meta:
        model = FeedbackTeachingAssistant
