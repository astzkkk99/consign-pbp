from django.db import models
import uuid

class Item(models.Model):
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="",null=False)
    item_type = models.CharField(max_length=255, default="")
    item_name = models.CharField(max_length=255, default="",null=False)
    item_price = models.IntegerField()
    item_description = models.TextField()
    