from django import forms
from .models import TablesModel


class EveningTables(forms.ModelForm):
    """ A Contact form """

    class Meta:
        """ Tables form meta """

        model = TablesModel
        fields = ["name", "email", "phone", "guests", "datetime", "message"]

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
    guests = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
    datetime = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={"class": "form-control text-dark", "type": "datetime-local"}
        ),
        label="Date and Time",
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control text-dark"})
    )
