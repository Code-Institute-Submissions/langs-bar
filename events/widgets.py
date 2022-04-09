from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    A custom clearable file input for
    add and edit event image field.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'events/custom_widget_templates/custom_clearable_file_input.html'
    )
