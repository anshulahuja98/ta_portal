from django.contrib import admin
from .models import AdministrativeStaffProfile, FacultyProfile, TeachingAssistantSupervisorProfile


@admin.register(FacultyProfile)
class FacultyAdmin(admin.ModelAdmin):
    class Meta:
        model = FacultyProfile
        fields = '__all__'


@admin.register(AdministrativeStaffProfile)
class AdministrativeStaffAdmin(admin.ModelAdmin):
    class Meta:
        model = AdministrativeStaffProfile
        fields = '__all__'


@admin.register(TeachingAssistantSupervisorProfile)
class TeachingAssistantSupervisorAdmin(admin.ModelAdmin):
    class Meta:
        model = TeachingAssistantSupervisorProfile
        fields = '__all__'
