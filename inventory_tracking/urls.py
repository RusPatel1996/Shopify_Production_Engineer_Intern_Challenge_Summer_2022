from django.urls import path

from . import views

app_name = 'inventory_tracking'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sku_number>/', views.item, name='item'),
]
