from django.urls import path
from . import views

urlpatterns = [
    path('', views.dresscode, name='dresscode'),
]
