from django.db import models
import uuid
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="",null=False)
    item_type = models.CharField(max_length=255, default="")
    item_name = models.CharField(max_length=255, default="",null=False)
    item_price = models.IntegerField()
    item_description = models.TextField()
    