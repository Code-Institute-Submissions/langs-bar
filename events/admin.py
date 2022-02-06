from django.contrib import admin
from .models import Month, Event

# Register your models here.


class MonthAdmin(admin.ModelAdmin):
    """ Admin Month Display Fields """
    list_display = ('name', 'friendly_name')

class EventAdmin(admin.ModelAdmin):
    """ Admin Event Display Fields """
    list_display = ('name', 'date')

admin.site.register(Month, MonthAdmin)
admin.site.register(Event, EventAdmin)
