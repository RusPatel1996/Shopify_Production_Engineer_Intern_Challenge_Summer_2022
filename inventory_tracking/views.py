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
    if not item_quantity:
        item_quantity = 1
    image = request.FILES['image'] if 'image' in request.FILES else None
    if sku_number and item_name:
        if request.POST.get("action") == "Add Item":
            Inventory.create_item(sku_number, item_name, item_quantity, image)
        elif request.POST.get("action") == "Update Item":
            Inventory.update_item(sku_number, item_name, item_quantity, image)
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
    Inventory.delete_item(sku_number)
    return HttpResponseRedirect(reverse('inventory_tracking:index'))
