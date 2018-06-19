from django.contrib import admin
from .models import TeachingAssistantProfile, FeedbackTeachingAssistant


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
    list_display = ['get_rollno', 'course', 'teaching_assistant_supervisor', 'approve']
    list_filter = ['teaching_assistant_supervisor', ]

    class Meta:
        model = FeedbackTeachingAssistant
