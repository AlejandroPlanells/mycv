from django.urls import path
from .views import *

app_name = "app_pages"

urlpatterns = [
    path("", InicioPageView.as_view(), name='inicio'),
    path("sobre-mi/", SobreMiPageView.as_view(), name='sobremi'),
    path("resumen/", ResumenPageView.as_view(), name='resumen'),
    path("contactar/", ContactarPageView.as_view(), name='contactar'),


]

