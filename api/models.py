from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='shop')
    tags = models.CharField(max_length=50)
    uploaded_by = models.CharField(max_length=50)

    def __str__(self):
        return self.name

