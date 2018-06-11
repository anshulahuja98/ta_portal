from django.contrib import admin
from .models import TeachingAssistantProfile


@admin.register(TeachingAssistantProfile)
class TeachingAssistantAdmin(admin.ModelAdmin):
    class Meta:
        model = TeachingAssistantProfile
        fields = '__all__'
