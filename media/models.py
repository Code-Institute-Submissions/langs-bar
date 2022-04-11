from django.db import models


class media(models.Model):
    """
    A Model for Media / Images to be uploaded
    cloudinary.
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)
