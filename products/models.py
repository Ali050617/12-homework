from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products_images')


    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])