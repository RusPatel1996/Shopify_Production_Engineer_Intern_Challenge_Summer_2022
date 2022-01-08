from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Inventory


def index(request):
    last_item = Inventory.latest_item()
    list_of_items = Inventory.objects.order_by('item_name')
    return render(request, 'inventory_tracking/index.html', {
        'list_of_items': list_of_items,
        'last_item': last_item,
    })


def create_update(request):
    sku_number = request.POST['sku_number']
    item_name = request.POST['item_name']
    item_quantity = request.POST['item_quantity']
    if sku_number and item_name and item_quantity:
        if request.POST.get("action") == "Add Item":
            Inventory.create_item(sku_number, item_name, item_quantity)
        elif request.POST.get("action") == "Update Item":
            Inventory.update_item(sku_number, item_name, item_quantity)
        else:
            Inventory.delete_item(sku_number)
    else:
        raise Http404("One of the fields is empty.")
    return HttpResponseRedirect(reverse('inventory_tracking:index'))


def update(request, sku_number):
    selected_item = Inventory.get_item(sku_number)
    list_of_items = Inventory.objects.order_by('item_name')
    return render(request, 'inventory_tracking/index.html', {
        'list_of_items': list_of_items,
        'last_item': selected_item,
    })


def delete(request, sku_number):
    if Inventory.item_exists(sku_number):
        Inventory.delete_item(sku_number)
    else:
        raise Http404("Cannot Delete")
    return HttpResponseRedirect(reverse('inventory_tracking:index'))
