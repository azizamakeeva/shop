from rest_framework import serializers

from apps.favorites.models import Favorite
from apps.products.models import Product
from apps.products.serializer import ProductSerializers
from apps.users.models import User


class FavoriteListSerializer(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = Favorite
        fields = ('id', 'products', 'user', )


class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', )

    def create(self, validated_data):
        user = self.context['request'].user
        user = User.objects.get(id=1)
        fav = Favorite.objects.create(user=user)
        fav.save()
        return fav


class FavoriteAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()



