from django.views.generic import View
import datetime
from .render import Render
from accounts.models import TeachingAssistantProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from courses.models import Feedback


@method_decorator(staff_member_required,name='dispatch')
class Pdf(View, LoginRequiredMixin):

    def get(self, request):
        month = datetime.datetime.now().strftime("%B")
        year = datetime.datetime.now().strftime("%Y")
        feedbacks = Feedback.objects.approved_current()
        params = {
            'feedbacks': feedbacks,
            'month': month,
            'year': year,
            'department': "Electrical Engineering"
        }
        return Render.render('frontend/pdf.html', params)
