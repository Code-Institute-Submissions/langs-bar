from django.contrib import admin
from .models import TablesModel

# Register your models here.


class EveningTablesAdmin(admin.ModelAdmin):
    """ Admin Contact Form Display Fields """
    list_display = ('name', 'email', 'datetime', 'guests')


admin.site.register(TablesModel, EveningTablesAdmin)
