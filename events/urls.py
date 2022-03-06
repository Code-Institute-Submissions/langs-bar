from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('vip/', views.all_vip, name='vip'),
    path('vip/<int:event_id>/', views.vip_detail, name='vip_detail'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
]
