from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, default="",null=False)
    item_type = models.CharField(max_length=255, default="")
    item_name = models.CharField(max_length=255, default="",null=False)
    item_price = models.IntegerField()
    item_description = models.TextField()
    