from django.db import models
from apps.categories.models import Category


class Product(models.Model):
    article = models.CharField(
        max_length=64,
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Артикль'
        verbose_name_plural = 'Артикли'

    def __str__(self):
        return f'id: {self.id} | article: {self.article}'


class ProductItem(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    size = models.CharField(
        max_length=255, blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    product = models.ForeignKey(
        Product,
        related_name='product_article',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    description = models.TextField(
        blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0,
        blank=True, null=True
    )
    quantity = models.PositiveIntegerField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)
    is_new = models.BooleanField(blank=True, null=True, default=False)
    bouquet_care = models.TextField(blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    product_id = models.ForeignKey(
        ProductItem,
        related_name='product_image',
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'
