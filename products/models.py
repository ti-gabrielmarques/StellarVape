from django.db import models


class Product(models.Model):
    name = models.CharField('Event Name', max_length=128)
    description = models.TextField(blank=True)
    price = models.FloatField(max_length=3)
    recommendation_level = models.IntegerField(null=True, blank=True)
    in_stock = models.BooleanField()

    def __str__(self):
        return self.name
