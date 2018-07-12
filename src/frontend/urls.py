from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView, TemplateView
from .views import ProfileDetailView, LoginView, CourseFeedbackView, CourseDetailView
from adminportal.views import Pdf
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

app_name = 'frontend'

urlpatterns = [
    path('details/', ProfileDetailView.as_view(), name='detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='frontend:login'), name='logout'),
    path('', RedirectView.as_view(pattern_name='frontend:detail')),
    path('past/', CourseDetailView.as_view(), name='past'),
    path('current/', CourseFeedbackView.as_view(), name='current'),
    path('timetable/', TemplateView.as_view(template_name='frontend/timetable.html'), name='timetable'),
    path('pdf/', Pdf.as_view(), name='pdf'),
    path('details/password-change/', PasswordChangeView.as_view(success_url='/details/password-change/done',
                                                                template_name='frontend/password_reset_form.html'),
         name='password_change'),
    path('details/password-change/done/',
         PasswordChangeDoneView.as_view(template_name='frontend/password_reset_done.html'),
         name='password_change_done')
]
