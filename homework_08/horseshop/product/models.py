from django.db import models

# Create your models here.
from category.models import Subcategory
from order.models import Order


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    site = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} {self.country}"


class ProductProperty(models.Model):
    BLACK = 'BK'
    WHITE = 'WT'
    BLUE = 'BL'
    BROWN = 'BR'
    RED = 'RD'
    COLORS = [
        (BLACK, 'Black'),
        (WHITE, 'White'),
        (BROWN, 'Brown'),
        (RED, 'Red')
    ]
    CHILD = 'C'
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (CHILD, 'Child'),
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    SIZES = [(38, '38'),
             (40, '40'),
             (42, '42'),
             (44, '44'),
             (46, '46')
             ]
    manufactured = models.IntegerField(default=0)
    color = models.CharField(max_length=2, choices=COLORS, default='BK')
    size = models.IntegerField(choices=SIZES, default=38)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')

    def __str__(self):
        return f"color:{self.color}, size:{self.size}, gender:{self.gender}"


class Product(models.Model):
    name = models.CharField(max_length=64)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    curr_price = models.DecimalField(max_digits=10, decimal_places=2)
    curr_count = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    property = models.OneToOneField('product.ProductProperty', on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"product{self.product.name} in order{self.order.primary_key}"
