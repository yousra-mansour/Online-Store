from statistics import mode
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='cat_photo%y%m%d', null=True)

    def __str__(self) -> str:
        return self.name


class Photos(models.Model):

    photo = models.ImageField(upload_to='pro_photo%y%m%d')


class Productos(models.Model):

    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    brand = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    color = models.CharField(max_length=50, null=True)
    specification = models.TextField(null=True)
    categories = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True)

    photos = models.ManyToManyField(Photos)

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-create']
