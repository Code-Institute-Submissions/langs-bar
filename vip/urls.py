from django.urls import path
from . import views


urlpatterns = [
    path('', views.vip, name='vip'),
    path('<booth_id>', views.vip_detail, name='vip_detail'),
]
