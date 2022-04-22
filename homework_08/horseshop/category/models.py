from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Subcategory(models.Model):
    name = models.CharField(max_length=32, unique=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"
