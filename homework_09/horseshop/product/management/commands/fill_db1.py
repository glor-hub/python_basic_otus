from django.core.management.base import BaseCommand

from product.models import (
    Product,
    ProductProperty,
    Manufacturer,
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        contacts = {'Eskadron': {'country': 'Germany',
                                 'phone': '+49 520 370 40',
                                 'email': 'info@pikeur.de'},
                    'Roeckl': {'country': 'Germany',
                               'phone': '+49 089 729 6958',
                               'email': 'kundenservice@roeckl.com'},
                    'Tommy Hilfiger': {'country': 'Switzerland',
                                       'phone': '810 800 866 694 45',
                                       'email': 'info:@globaltommy.com'},
                    'Amahorse': {'country': 'Italy',
                                 'phone': '+39 075 856 0191',
                                 'email': 'info@amahorse.com'}
                    }
        companies = [
            'Eskadron',
            'Roeckl',
            'Tommy Hilfiger',
            'Amahorse'
        ]
        for company in companies:
            Manufacturer.objects.get_or_create(name=company,
                                               country=contacts[company]["country"],
                                               phone=contacts[company]["phone"],
                                               email=contacts[company]["email"]
                                               )

