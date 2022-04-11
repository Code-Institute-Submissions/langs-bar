from django.db import models


class MenuImages(models.Model):
    """
    A model to upload images for menus
    which can be displayed in a carousel.
    """

    class Meta:
        """ Display name correctly in admin """
        verbose_name_plural = 'Menu Images'

    name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
