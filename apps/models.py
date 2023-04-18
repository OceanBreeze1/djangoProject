from django.db import models

from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()


