from accounts.models import TeachingAssistantProfile
from django.views.generic import View, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from .forms import ApprovalForm
from django.views.generic.edit import FormView


class UserObjectMixin(object):
    def get_object(self):
        return get_object_or_404(TeachingAssistantProfile, user=self.request.user)


class LoginView(DefaultLoginView):
    template_name = 'frontend/login.html'


class DashboardView(LoginRequiredMixin, UserObjectMixin, DetailView):
    context_object_name = 'profile'
    model = TeachingAssistantProfile
    template_name = 'frontend/dashboard.html'


class ApprovalFormView(FormView):
    template_name = 'frontend/course.html'
    form_class = ApprovalForm
    success_url = '/dashboard/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['teaching_assistant'] = TeachingAssistantProfile.objects.get(user=self.request.user)
        kwargs['course'] = Course.objects.get(slug=self.kwargs.get('slug'))
        return kwargs


class CourseDetailView(DetailView):
    template_name = 'frontend/course.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['feedbacks'] = self.get_object().feedbackteachingassistant_set.filter(
            teaching_assistant__user=self.request.user)
        context['form'] = ApprovalForm()
        return context


class CourseFeedbackView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = CourseDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ApprovalFormView.as_view()
        return view(request, *args, **kwargs)
