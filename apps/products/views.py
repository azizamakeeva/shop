from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.products.models import Product, ProductItem, ProductImage
from apps.products.serializer import ProductSerializers, ProductItemSerializers, ProductImageSerializers


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['article']
    ordering_fields = ['article']


class ProductItemAPIViewSet(ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['category', 'is_new']
    search_fields = ['title', 'size', 'discount',
                     'description', 'equipment', 'bouquet_care', 'specifications', 'discount'
                     ]

    ordering_fields = ['title', 'size', 'discount', 'description',
                       'equipment', 'bouquet_care', 'specifications', 'discount'
                       ]


class ProductImageAPIViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers
