from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Inventory


def index(request):
    print(Inventory.get_list_of_items().values())
    list_of_items = Inventory.objects.order_by('item_name')
    context = {'list_of_items': list_of_items}
    return render(request, 'inventory_tracking/index.html', context)


def item(request, sku_number):
    if Inventory.item_exists(sku_number):
        resulting_item = Inventory.get_item(sku_number)
        return render(request, 'inventory_tracking/item.html', {
            'sku_number': resulting_item.sku_number,
            'item_name': resulting_item.item_name,
            'item_quantity': resulting_item.item_quantity,
        })
    raise Http404("sku number doesn't exist.")
