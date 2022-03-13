from django.db import models

# Create your models here.


class Month(models.Model):
    """ A Model for months category """

    class Meta:
        """ Verbose name for admin """
        verbose_name_plural = 'Month'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_friendly_name(self):
        """ Get friendly / front end name """
        return f"{self.friendly_name}"


class Event(models.Model):
    """ A Model for events """
    month = models.ForeignKey('Month', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    date = models.CharField(max_length=254)
    booth_size = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date}"
