from django.urls import path

from frontend.views import HomeView

urlpatterns = [
    path('', HomeView.as_view())
]
