from django.db import models, IntegrityError


class Inventory(models.Model):
    sku_number = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_quantity = models.IntegerField(default=1)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.item_name

    @classmethod
    def create_item(cls, sku, name, quantity, image=None):
        created = False
        try:
            cls.objects.create(sku_number=sku, item_name=name, item_quantity=quantity, image=image)
            created = True
        except IntegrityError as e:
            print(e)
        return created

    @classmethod
    def get_item(cls, sku):
        item = None
        try:
            item = cls.objects.get(sku_number=sku)
        except cls.DoesNotExist as e:
            print(e)
        except cls.MultipleObjectsReturned as e:
            print(e)
        return item

    @classmethod
    def get_list_of_items(cls):
        return cls.objects.all()

    @classmethod
    def update_item(cls, sku, name, quantity, image=None):
        item = Inventory.get_item(sku)
        if item:
            item.item_name = name
            item.item_quantity = quantity
            item.image = image
            item.save()
            return True
        return False

    @classmethod
    def delete_item(cls, sku):
        item = Inventory.get_item(sku)
        if item:
            Inventory.delete(item)
            return True
        return False

    @classmethod
    def item_exists(cls, sku):
        if Inventory.get_item(sku):
            return True
        return False

    @classmethod
    def latest_item(cls):
        item = None
        try:
            item = cls.objects.latest('sku_number')
        except cls.DoesNotExist as e:
            print(e)
        return item
