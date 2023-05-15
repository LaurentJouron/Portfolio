from django.urls import path
from . import views


urlpatterns = [
    path("", views.reception, name='reception'),
    path("index/", views.index, name='index'),
]
