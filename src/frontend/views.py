# from accounts.models import TeachingAssistantProfile
# from django.views.generic.base import TemplateView
# from django.shortcuts import get_object_or_404
#
# class UserObjectMixin(object):
#     def get_object(self, queryset=None):
#         user_id = get_object_or_404(User, username=self.kwargs.get('ignumber'))
#         return get_object_or_404(UserProfile, user=user_id)
#
# class DashboardView(UserObjectMixin):
#     model = TeachingAssistantProfile
#     template_name = 'frontend/dashboard.html'
