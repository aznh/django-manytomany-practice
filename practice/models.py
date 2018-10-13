from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()
    tags = models.ManyToManyField(Tag)