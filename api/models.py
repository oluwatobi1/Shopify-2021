from django.db import models

# Create your models here.
from django.utils import timezone


class Shop(models.Model):
    description = models.TextField(max_length=100)
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='shop')
    tags = models.CharField(max_length=50)
    uploaded_by = models.CharField(max_length=50)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tags

