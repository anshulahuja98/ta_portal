from accounts.models import TeachingAssistantProfile, FeedbackTeachingAssistant
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course


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


class CourseFeedbackView(LoginRequiredMixin, DetailView):
    context_object_name = 'course'
    model = Course
    template_name = 'frontend/course.html'

    def get_context_data(self, **kwargs):
        context = super(CourseFeedbackView, self).get_context_data(**kwargs)
        # course = str(self.object.user.username)
        user = self.request.user
        feedbacks = FeedbackTeachingAssistant.objects.filter(ta__user__username=user).filter(
            course__course_code=self.object.course_code)
        profile = get_object_or_404(TeachingAssistantProfile, user=self.request.user)
        context['feedbacks'] = feedbacks
        context['user'] = user
        context['profile'] = profile
        return context
