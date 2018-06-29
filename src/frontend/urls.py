from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import DetailView, LoginView, CourseFeedbackView, CourseDetailView
from adminportal.views import Pdf

app_name = 'frontend'

urlpatterns = [
    path('details/', DetailView.as_view(), name='detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='frontend:login'), name='logout'),
    # path('passwordreset/', auth_views.PasswordResetView, name='passwordreset'),
    path('', RedirectView.as_view(pattern_name='frontend:detail')),
    path('past/', CourseDetailView.as_view(), name='past'),
    path('current/', CourseFeedbackView.as_view(), name='current'),
    path('pdf/', Pdf.as_view(), name='pdf'),
    # path('course/<slug>/', CourseFeedbackView.as_view(), name='course-detail')
]
