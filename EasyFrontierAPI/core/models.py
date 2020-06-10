from django.db import models

# Create your models here.

class Medicines(models.Model):
    code = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    cost = models.CharField(max_length=20, null=True, blank=True)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    availability = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'sis_medicine'
        verbose_name = 'Remédio - Dados'
        verbose_name_plural = 'Remédios - Dados'