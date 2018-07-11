from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code',)

    class Meta:
        model = Course
        exclude = ('slug',)
