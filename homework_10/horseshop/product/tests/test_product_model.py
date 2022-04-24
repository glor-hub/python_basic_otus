from django.test import TestCase

from product.models import Product, Manufacturer


class ManufacturerModelTest(TestCase):
    fixtures = ["product.json"]

    @classmethod
    def setUpTestData(cls):
        cls.manufacturer = Manufacturer.objects.get(
            id=1
        )

    def test_manufacturer_count(self):
        manufact_count = Manufacturer.objects.count()
        self.assertEqual(4, manufact_count)

    def test_manufacturer_string_representation(self):
        full_name = f"{self.manufacturer.name} {self.manufacturer.country}"
        self.assertEquals(str(self.manufacturer), full_name)


class ProductModelTest(TestCase):
    fixtures = ["product.json"]

    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.get(
            id=1
        )

    def test_products_count(self):
        products_count = Product.objects.count()
        self.assertEqual(4, products_count)

    def test_product_string_representation(self):
        prod_name = f"{self.product.name}"
        self.assertEquals(str(self.product), prod_name)
