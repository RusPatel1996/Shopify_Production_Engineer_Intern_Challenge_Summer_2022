from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Inventory

MAX_INT = 2**31-1
MIN_INT = -2**31

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
    if not item_quantity or item_quantity < '0':
        item_quantity = '0'
    if sku_number < '0':
        raise Http404("SKU Number cannot be below 0")
    if not within_bounds(sku_number):
        raise Http404("SKU number is out of bounds.")
    if not within_bounds(item_quantity):
        raise Http404("Item quantity is out of bounds.")
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


def within_bounds(number):
    if MAX_INT < int(number) < MIN_INT:
        return False
    return True
