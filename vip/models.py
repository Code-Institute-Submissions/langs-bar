from django.db import models

# Create your models here.


PARTY_SIZE = (
    ('4-5', '4-6'),
    ('6-8', '6-8'),
    (' ', ' '),
)


class Booth(models.Model):
    """ A Model to create VIP BOOTHS """

    party_size = models.CharField(
        max_length=3,
        choices=PARTY_SIZE,
        default=' '
    )
    date = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.party_size} - {self.price}"
