from django.forms import ModelForm
from main.models import Item
from django.utils.html import strip_tags

class ItemEntryForm(ModelForm):
    class Meta:
        model = Item
        fields = ["item_type", "item_name", "item_price", "item_description"]
        
        
        
    def clean_item_name(self):
        item_name = self.cleaned_data["item_name"]
        return strip_tags(item_name)

    def clean_item_type(self):
        item_type = self.cleaned_data["item_type"]
        return strip_tags(item_type)
    
    def clean_item_price(self):
        item_price = self.cleaned_data["item_price"]
        return strip_tags(item_price)
    
    def clean_item_description(self):
        item_description = self.cleaned_data["item_description"]
        return strip_tags(item_description)