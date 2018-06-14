from accounts.models import TeachingAssistantProfile
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from django.urls import reverse, reverse_lazy


class UserObjectMixin(object):
    def get_object(self):
        return get_object_or_404(TeachingAssistantProfile, user=self.request.user)


class LoginView(DefaultLoginView):
    model = TeachingAssistantProfile
    template_name = 'frontend/login.html'


class DashboardView(LoginRequiredMixin, UserObjectMixin, DetailView):
    context_object_name = 'profile'
    model = TeachingAssistantProfile
    template_name = 'frontend/dashboard.html'


class CourseView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/course.html'
    context_object_name = 'course'
    model = Course
