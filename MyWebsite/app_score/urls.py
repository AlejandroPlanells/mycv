from django.urls import path

from .views import *
from . import views
app_name = 'app_score'

urlpatterns = [
    path("", HomePageView.as_view(), name='inicio'),
    path("cs/", views.test, name='test'),
]




