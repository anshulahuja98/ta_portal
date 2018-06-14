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
