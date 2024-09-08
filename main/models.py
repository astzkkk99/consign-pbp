from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    item_price = models.IntegerField()
    item_description = models.TextField()
    