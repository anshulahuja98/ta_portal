from django.views.generic import View
import datetime
from .render import Render
from accounts.models import TeachingAssistantProfile


class Pdf(View):

    def get(self, request):
        # program =
        month = datetime.datetime.now().strftime("%B")
        year = datetime.datetime.now().strftime("%Y")
        students = TeachingAssistantProfile.objects.all()
        params = {
            'students': students,
            'month': month,
            'year': year
        }
        return Render.render('frontend/pdf.html', params)
