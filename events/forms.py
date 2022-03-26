from django import forms
from .widgets import CustomClearableFileInput
from .models import Event, Month


class EventForm(forms.ModelForm):
    """ An admin add event form """
    class Meta:
        """ EventForm Meta """
        model = Event
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        months = Month.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in months]

        self.fields['month'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-white text-dark'
