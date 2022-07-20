from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=300)


class Product(models.Model):
    title = models.CharField(max_length=250)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    mfg_date = models.DateTimeField()
    exp_date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

