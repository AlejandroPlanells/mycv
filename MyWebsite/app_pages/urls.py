from django.urls import path
from .views import *
from . import views

app_name = "app_pages"

urlpatterns = [
    path("", InicioPageView.as_view(), name='inicio'),
    path("sobre-mi/", SobreMiPageView.as_view(), name='sobremi'),
    path("resumen/", ResumenPageView.as_view(), name='resumen'),
    path("contactar/", ContactarPageView.as_view(), name='contactar'),

    path('user_settings/', views.userSettings, name="user_settings"),
    path('update_theme/', views.updateTheme, name="update_theme"),


]

