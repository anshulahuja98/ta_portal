from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

app_name = 'frontend'

urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name='frontend/dashboard.html'), name='home'),
    path('login/', auth_views.login, {'template_name': 'frontend/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'frontend/login.html'}, name='logout'),
    path('', RedirectView.as_view(pattern_name='frontend:login'))
]
