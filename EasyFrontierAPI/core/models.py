from django.db import models

# Create your models here.

class ProductType(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return str(self.status)

    class Meta:
        db_table = 'sis_product_type'
        verbose_name = 'Produto - Tipo'
        verbose_name_plural = 'Produto - Tipos'

class Medicines(models.Model):
    code = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    cost = models.CharField(max_length=20, null=True, blank=True)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    availability = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'sis_medicine'
        verbose_name = 'Remédio - Dados'
        verbose_name_plural = 'Remédios - Dados'


class Order(models.Model):
    code = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.code)

    class Meta:
        db_table = 'sis_order'
        verbose_name = 'Pedido - Dados'
        verbose_name_plural = 'Pedido - Dados'