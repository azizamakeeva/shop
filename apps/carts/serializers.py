from rest_framework import serializers
from apps.carts.models import Cart, CartItem
from apps.products.serializer import ProductItemSerializers


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'id',
            'product',
            'amount'
        )


class CartItemDetailSerializers(serializers.ModelSerializer):
    product = ProductItemSerializers(read_only=True)

    class Meta:
        model = CartItem
        fields = (
            'id',
            'product',
            'amount'
        )


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemDetailSerializers(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = (
            'id', 'user', 'cart_items',
        )
