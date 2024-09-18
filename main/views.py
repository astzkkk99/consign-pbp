from django.shortcuts import render, redirect
from main.forms import ItemEntryForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    item_entries = Item.objects.all()
    
    context = {
        'title' : "CONSIGN!",
        'item_type' : "Console",
        'item_name' : "PS4",
        'item_price': '2000000',
        'item_description': "PS4 bekas, udah dipake 4 tahun, minus lecet aja",
        'item_entries' : item_entries,
    }

    return render(request, "main.html", context)

def create_item_entry(request):
    form  = ItemEntryForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")