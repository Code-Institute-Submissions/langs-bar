from django.contrib import admin
from .models import Booth

# Register your models here.


class BoothAdmin(admin.ModelAdmin):
    """ Admin Display Fields """
    list_display = ('date', 'party_size', 'price', 'quantity')


admin.site.register(Booth, BoothAdmin)
