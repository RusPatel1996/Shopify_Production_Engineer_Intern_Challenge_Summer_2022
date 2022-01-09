from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'inventory_tracking'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_update', views.create_update, name='create_update'),
    path('update/<int:sku_number>', views.update, name='update'),
    path('delete/<int:sku_number>/', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
