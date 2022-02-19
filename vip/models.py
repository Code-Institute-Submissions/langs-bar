from django.db import models

# Create your models here.


class MonthVip(models.Model):
    """ A Model for vip months category """

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


class Booth(models.Model):
    """ A Model to create VIP BOOTHS """

    month = models.ForeignKey('MonthVip', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=254, null=True, blank=True)
    guests = models.CharField(max_length=254, null=True, blank=True)
    quantity_available = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.guests} - {self.quantity_available} - {self.price}"
