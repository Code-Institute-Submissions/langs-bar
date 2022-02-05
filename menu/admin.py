from django.contrib import admin
from .models import MenuImages

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    """ Admin Display Fields """
    list_display = ('name', 'image')


admin.site.register(MenuImages, MenuAdmin)
