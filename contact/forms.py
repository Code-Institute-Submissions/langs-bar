from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    """
    A Contact form which allows users
    to contact the site admin.
    """

    class Meta:
        """ Contact form meta """
        model = ContactModel
        fields = [
            "name",
            "email",
            "phone",
            "message"
        ]

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
