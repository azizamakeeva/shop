from django.contrib.auth import get_user_model
from django.db import models

from apps.carts.models import Cart
from utils.validators import phone_number_validators

User = get_user_model()

PAYMENT_TYPE_CHOICES = (
    ('cart', "cart"),
    ('money', 'money'),
)


class Order(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='order_cart',
        blank=True, null=True,
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_order',
        blank=True, null=True,
    )
    address = models.CharField(
        blank=True, null=True, max_length=255,
    )
    last_name = models.CharField(
        max_length=255, blank=True, null=True,
    )
    first_name = models.CharField(
        max_length=255, blank=True, null=True,
    )
    email = models.EmailField(
        max_length=255, blank=True, null=True,
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[phone_number_validators],
        blank=True, null=True,
    )
    comment = models.TextField(
        blank=True, null=True,
    )
    payment_type = models.CharField(
        choices=PAYMENT_TYPE_CHOICES,
        null=True, blank=True, max_length=25,
    )
    total_sum = models.DecimalField(
        decimal_places=2, blank=True, null=True,
        default=0, max_digits=10
    )

    def __str__(self):
        return f"{self.first_name} -- {self.last_name} -- {self.address}"


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_product', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, default=0, max_digits=10, blank=True, null=True)
