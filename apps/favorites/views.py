from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from apps.favorites.models import Favorite
from apps.favorites.serializers import FavoriteListSerializer, FavoriteCreateSerializer, \
    FavoriteAddSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from apps.products.models import Product
from apps.users.models import User


class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return FavoriteListSerializer

        if self.action == 'retrieve':
            return FavoriteListSerializer

        if self.action == 'create':
            return FavoriteCreateSerializer

        return FavoriteCreateSerializer

    # ЭТОТ ЕНДПОИНТ ДЛЯ ДОБАВЛЕНИЯ И УДАЛЕНИЯ ПРОДУКТОВ ИЗ ИЗБРАННЫХ
    # ЕСЛИ ОДИН И ТОТ ЖЕ ПРОДУКТ ДОБАВИТЬ ДВА РАЗА - ОН УДАЛИТСЯ
    @swagger_auto_schema(responses={200: FavoriteListSerializer()}, request_body=FavoriteAddSerializer)
    @action(detail=True, methods=['put'])
    def add_or_remove_favorite(self, request, pk=None):
        serializer = FavoriteAddSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            product_to_add = Product.objects.filter(id=request.data['product_id']).first()
            favorite_obj = self.get_object()

            if favorite_obj.products.filter(id=product_to_add.id).exists():
                favorite_obj.products.remove(product_to_add)
                favorite_obj.save()
                return Response(data=FavoriteListSerializer(favorite_obj).data)

            favorite_obj.products.add(product_to_add)
            favorite_obj.save()
            return Response(data=FavoriteListSerializer(favorite_obj).data)

    @swagger_auto_schema(responses={200: FavoriteListSerializer()})
    @action(detail=False, methods=['get'])
    def get_my_favorites(self, request):
        user = User.objects.get(id=1)
        users_favs = Favorite.objects.filter(user=user)
        return Response(FavoriteListSerializer(users_favs, many=True).data)
