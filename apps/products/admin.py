from django.contrib import admin
from apps.products.models import Product, ProductItem

admin.site.register(Product)
admin.site.register(ProductItem)
