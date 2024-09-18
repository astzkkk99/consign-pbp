from django.forms import ModelForm
from main.models import Item

class ItemEntryForm(ModelForm):
    class Meta:
        model = Item
        fields = ["item_type", "item_name", "item_price", "item_description"]