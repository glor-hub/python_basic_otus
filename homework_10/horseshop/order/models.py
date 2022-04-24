from django.db import models

# Create your models here.
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32, default='')
    email = models.EmailField(max_length=64, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    CREATED = 'C'
    ACTIVE = 'A'
    FINISHED = 'F'
    STATUS = [
        (CREATED, 'Created'),
        (ACTIVE, 'Active'),
        (FINISHED, 'Finished')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_created=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now_add=False)
    status = models.CharField(max_length=1, choices=STATUS, default='C')
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"order {self.pk} status {self.status}"
