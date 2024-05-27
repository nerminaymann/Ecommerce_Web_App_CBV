from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True,on_delete=models.PROTECT)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    #type is meaning is downloadable or not
    type = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey('Category',null=True, blank=True,on_delete=models.SET_NULL)
    # image = models.ImageField(
    #     upload_to=''
    # )

    def __str__(self):
        return self.name







