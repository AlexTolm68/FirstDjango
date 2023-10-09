from django.db import models


# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=32)


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=200, default="описание")
    count = models.PositiveIntegerField()
    colors = models.ManyToManyField(to=Color)

    def __repr__(self):
        return f"Item({self.name}, {self.brand}, {self.count})"
