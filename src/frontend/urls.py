from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import DashboardView, LoginView, CourseFeedbackView, ApprovalFormView

app_name = 'frontend'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='frontend:login'), name='logout'),
    path('', RedirectView.as_view(pattern_name='frontend:dashboard')),
    path('course/<slug>/', CourseFeedbackView.as_view(), name='course-detail'),
    path('form/', ApprovalFormView.as_view(), name='approval-form'),
]
