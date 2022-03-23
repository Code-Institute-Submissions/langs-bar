from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
]
