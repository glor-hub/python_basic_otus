from django.core.management.base import BaseCommand

from product.models import (
    Product,
    ProductProperty,
    Manufacturer,
)



class Command(BaseCommand):

    def handle(self, *args, **options):

        goods = {'saddle pad "COTTON" DR': {'price': 500,
                                            'count': 29,
                                            'manufacturer': Manufacturer(id=1)},
                 'gloves "TRYON"': {'price': 150,
                                    'count': 8,
                                    'manufacturer': Manufacturer(id=2)},
                 'breeches "Performans"': {'price': 378,
                                           'count': 17,
                                           'manufacturer': Manufacturer(id=3)},
                 'helmet "EQUESTRO FRAME"': {'price': 450,
                                             'count': 3,
                                             'manufacturer': Manufacturer(id=4)}
                 }
        products = [
            'saddle pad "COTTON" DR',
            'gloves "TRYON"',
            'breeches "Performans"',
            'helmet "EQUESTRO FRAME"'
        ]
        for product in products:
            Product.objects.get_or_create(name=product,
                                          curr_price=goods[product]["price"],
                                          curr_count=goods[product]["count"],
                                          manufacturer=goods[product]["manufacturer"]
                                          )
