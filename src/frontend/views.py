from accounts.models import TeachingAssistantProfile
from django.views.generic import View, DetailView, CreateView
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from .forms import ApprovalForm


class UserObjectMixin(object):
    def get_object(self):
        return get_object_or_404(TeachingAssistantProfile, user=self.request.user)


class LoginView(DefaultLoginView):
    template_name = 'frontend/login.html'


class DetailView(LoginRequiredMixin, UserObjectMixin, DetailView):
    context_object_name = 'profile'
    model = TeachingAssistantProfile
    template_name = 'frontend/details.html'


class ApprovalRequestView(CreateView):
    template_name = 'frontend/past.html'
    form_class = ApprovalForm

    def get_success_url(self):
        return reverse('frontend:course-detail', kwargs={'slug': self.kwargs.get('slug', None)})

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        self.request.POST.update({
            'teaching_assistant': TeachingAssistantProfile.objects.get(user=self.request.user).id,
            'course': Course.objects.get(slug=self.kwargs.get('slug', None)).id
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)


class CourseDetailView(DetailView):
    template_name = 'frontend/past.html'
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
        view = ApprovalRequestView.as_view()
        return view(request, *args, **kwargs)
