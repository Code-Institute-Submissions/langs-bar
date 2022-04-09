from django.db import models

# Create your models here.


class ContactModel(models.Model):
    """
    A model to allow admin to
    view customer contact forms.
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=200)

    class Meta:
        """ Verbose name for admin """
        verbose_name_plural = 'Contact Form'

    def __str__(self):
        return f"{self.name} - {self.email}"
