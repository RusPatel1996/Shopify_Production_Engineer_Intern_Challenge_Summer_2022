from django.urls import path

from . import views

app_name = 'inventory_tracking'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sku_number>/', views.item, name='item'),
    path('create_update_delete', views.create_update_delete, name='create_update_delete'),
]
