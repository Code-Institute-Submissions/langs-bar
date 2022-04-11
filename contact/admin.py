from django.contrib import admin
from .models import ContactModel


class ContactAdmin(admin.ModelAdmin):
    """ Admin Contact Form Display Fields """
    list_display = ('name', 'email', 'phone')


admin.site.register(ContactModel, ContactAdmin)
