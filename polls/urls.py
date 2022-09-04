from django.urls import path

from . import views

urlpatterns = [
    path('', views.customIndex, name='Custom Index'),
]