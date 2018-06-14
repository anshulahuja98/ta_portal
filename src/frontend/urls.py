from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import DashboardView, LoginView, CourseView

app_name = 'frontend'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.logout, {'template_name': 'frontend/login.html'}, name='logout'),
    path('', RedirectView.as_view(pattern_name='frontend:login')),
    path('course/<slug>/', CourseView.as_view(), name='course-detail'),
]
