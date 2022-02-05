from django.db import models

# Create your models here.


class MenuImages(models.Model):
    """ A model to upload images for menus """

    class Meta:
        """ Display name correctly in admin """
        verbose_name_plural = 'Menu Images'

    name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
