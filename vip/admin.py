from django.contrib import admin
from .models import MonthVip, Booth

# Register your models here.


class MonthVipAdmin(admin.ModelAdmin):
    """ Admin Month Display Fields """
    list_display = ('name', 'friendly_name')

class BoothAdmin(admin.ModelAdmin):
    """ Admin Display Fields """
    list_display = ('date', 'guests', 'price', 'quantity_available')

admin.site.register(MonthVip, MonthVipAdmin)
admin.site.register(Booth, BoothAdmin)
