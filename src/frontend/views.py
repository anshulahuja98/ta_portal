from accounts.models import TeachingAssistantProfile
from django.views.generic import View, CreateView
from django.views.generic import DetailView as DefaultDetailView
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from .forms import ApprovalForm
import datetime


class UserObjectMixin(object):
    def get_object(self):
        return get_object_or_404(TeachingAssistantProfile, user=self.request.user)


class LoginView(DefaultLoginView):
    template_name = 'frontend/login.html'


class DetailView(LoginRequiredMixin, UserObjectMixin, DefaultDetailView):
    context_object_name = 'profile'
    model = TeachingAssistantProfile
    template_name = 'frontend/details.html'


class CourseDetailView(DefaultDetailView, UserObjectMixin):
    template_name = 'frontend/past.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['feedbacks'] = self.get_object().feedbackteachingassistant_set.filter(
            teaching_assistant__user=self.request.user)
        return context


class ApprovalRequestView(CreateView, UserObjectMixin):
    template_name = 'frontend/current.html'
    form_class = ApprovalForm

    def get_success_url(self):
        return reverse('frontend:current')

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        self.request.POST.update({
            'teaching_assistant': TeachingAssistantProfile.objects.get(user=self.request.user).id,
            'teaching_assistant_supervisor': TeachingAssistantProfile.objects.get(
                user=self.request.user).teaching_assistant_supervisor.id,
            'month': datetime.datetime.now().month,
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)


class CourseApprovalDetailView(DetailView, UserObjectMixin):
    template_name = 'frontend/past.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = ApprovalForm()
        context['current_month'] = datetime.datetime.now().strftime("%B")
        context['current_year'] = datetime.datetime.now().strftime("%Y")
        current_feedback = self.get_object().feedbackteachingassistant_set.filter(
            teaching_assistant__user=self.request.user, month=datetime.date.today().month)
        if current_feedback[0].approve is True:
            check_feedback_status = 1
            context['current_feedback'] = current_feedback[0].duty_completed

        elif current_feedback[0].approve is False:
            check_feedback_status = -1
            context['current_feedback'] = current_feedback[0].duty_completed
        else:
            check_feedback_status = 0

        context['check_feedback_status'] = check_feedback_status
        context['form'] = ApprovalForm()
        return context


class CourseFeedbackView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = CourseApprovalDetailView.as_view(template_name='frontend/current.html')
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ApprovalRequestView.as_view(template_name='frontend/current.html')
        return view(request, *args, **kwargs)
