from rest_framework.routers import DefaultRouter

from apps.products.views import ProductAPIViewSet, ProductImageAPIViewSet, ProductItemAPIViewSet

router = DefaultRouter()
router.register('products', ProductAPIViewSet, basename='products')
router.register('products_item', ProductItemAPIViewSet, basename='products_item')
router.register('products_image', ProductImageAPIViewSet, basename='products_image')

urlpatterns = router.urls
