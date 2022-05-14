from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models import ProductItem

User = get_user_model()


class CartManager(models.Manager):
    def get_or_new(self, request):
        user = request.user
        cart_id = request.session.get('cart_id', None)
        if user is not None and user.is_authenticated:
            if user.cart:
                cart_obj = request.user.cart
            else:
                cart_obj = Cart.objects.get(pk=cart_id)
                cart_obj.user = user
                cart_obj.save()
            return cart_obj
        else:
            cart_obj = Cart.objects.get_or_create(pk=cart_id)
            cart_id = request.session['cart_id'] = cart_obj[0].id
            return cart_obj[0]


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='cart'
    )
    objects = CartManager()

    def __str__(self):
        return f"Cart owner is {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='cart_items',
    )
    product = models.ForeignKey(
        ProductItem, on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='product_item_cart'
    )
    amount = models.PositiveIntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return f"{self.cart.id} -- {self.product.title} -- {self.amount}"

    @receiver(post_save, sender=User)
    def create_cart_model(sender, instance, created, **kwargs):
        if created:
            Cart.objects.create(user=instance)
