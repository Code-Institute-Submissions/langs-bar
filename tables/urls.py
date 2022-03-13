from django.urls import path
from . import views

urlpatterns = [
    path('', views.evening_table_form, name='tables'),
]
