from django.utils import timezone

from accounts.models import TeachingAssistantProfile
from django.views.generic import View, CreateView, TemplateView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course, Feedback
from .forms import ApprovalForm

import datetime
from django.views.generic.edit import UpdateView


class UserObjectMixin(object):
    def get_object(self):
        return get_object_or_404(TeachingAssistantProfile, user=self.request.user)


class LoginView(DefaultLoginView):
    template_name = 'frontend/login.html'


class ProfileDetailView(UpdateView, LoginRequiredMixin):
    model = TeachingAssistantProfile
    fields = ['roll_no', 'program', 'phone', 'alternate_pno', 'research_area', 'ug_course', 'pg_course']
    template_name = 'frontend/details.html'

    def get_object(self, queryset=None):
        return get_object_or_404(TeachingAssistantProfile, user=self.request.user)


class CourseDetailView(UserObjectMixin, DetailView):
    template_name = 'frontend/past.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['feedbacks'] = self.get_object().feedback_set.filter(
            teaching_assistant__user=self.request.user)
        return context


class ApprovalRequestView(UserObjectMixin, CreateView):
    template_name = 'frontend/current.html'
    form_class = ApprovalForm

    def get_success_url(self):
        return reverse('frontend:current')

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        teaching_assistant_profile = TeachingAssistantProfile.objects.get(user=self.request.user)
        try:
            teaching_assistant_supervisor_id = teaching_assistant_profile.teaching_assistant_supervisor.id
        except AttributeError:
            teaching_assistant_supervisor_id = None
        self.request.POST.update({
            'teaching_assistant': teaching_assistant_profile.id,
            'teaching_assistant_supervisor': teaching_assistant_supervisor_id
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)


class CourseApprovalDetailView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile'] = TeachingAssistantProfile.objects.get(user=self.request.user)
        context['no_feedback_courses'] = self.get_excluded_courses()
        context['form'] = ApprovalForm()
        context['time_now'] = datetime.datetime.now()
        return context

    def get_excluded_courses(self):
        return set(Course.objects.filter(teaching_assistants__user=self.request.user)) - set(
            Course.objects.filter(
                id__in=Feedback.objects.filter(teaching_assistant__user=self.request.user,
                                               requested_on__month=timezone.now().month).values_list('course')))


class CourseFeedbackView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = CourseApprovalDetailView.as_view(template_name='frontend/current.html')
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ApprovalRequestView.as_view(template_name='frontend/current.html')
        return view(request, *args, **kwargs)
