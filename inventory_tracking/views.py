from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Inventory


def index(request):
    last_item = Inventory.latest_item()
    list_of_items = Inventory.objects.order_by('item_name')
    if last_item:
        return render(request, 'inventory_tracking/index.html', {
            'list_of_items': list_of_items,
            'last_item': last_item,
            'latest_sku_number': last_item.sku_number,
            'latest_item_name': last_item.item_name,
            'latest_item_quantity': last_item.item_quantity,
        })
    else:
        return render(request, 'inventory_tracking/index.html', {
            'list_of_items': list_of_items,
            'last_item': last_item,
        })


def create_or_update(request):
    sku_number = request.POST['sku_number']
    item_name = request.POST['item_name']
    item_quantity = request.POST['item_quantity']
    if request.POST.get("action") == "Add Item":
        Inventory.create_item(sku_number, item_name, item_quantity)
    else:
        Inventory.update_item(sku_number, item_name, item_quantity)
    return HttpResponseRedirect(reverse('inventory_tracking:index'))


def item(request, sku_number):
    if Inventory.item_exists(sku_number):
        resulting_item = Inventory.get_item(sku_number)
        return render(request, 'inventory_tracking/item.html', {
            'sku_number': resulting_item.sku_number,
            'item_name': resulting_item.item_name,
            'item_quantity': resulting_item.item_quantity,
        })
    raise Http404("sku number doesn't exist.")
