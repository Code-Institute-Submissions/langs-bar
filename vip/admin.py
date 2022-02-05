from django.contrib import admin
from .models import Booth

# Register your models here.


class BoothAdmin(admin.ModelAdmin):
    list_display = ('date', 'party_size', 'price')


admin.site.register(Booth, BoothAdmin)
