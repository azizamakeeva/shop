from django.db import models

# Create your models here.
from apps.products.models import Product
from apps.users.models import User


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

