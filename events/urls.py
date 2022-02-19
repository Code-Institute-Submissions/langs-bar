from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<event_id>', views.event_detail, name='event_detail'),
    path('vip/', views.all_vip, name='vip'),
    path('vip/<event_id>/', views.vip_detail, name='vip_detail'),
]
