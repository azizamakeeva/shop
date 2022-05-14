from rest_framework import generics

from apps.orders.models import Order, ProductOrder
from apps.orders.serializers import OrderSerializer, OrderDetailSerializer
from utils.celery_tasks import send_order


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = self.request.user
        summa = 0
        for item in user.cart.cart_items.all():
            product_item = item.product
            product_order = ProductOrder.objects.create(
                order=serializer.save(),
                title=product_item.title,
                quantity=item.amount,
                price=product_item.price
            )
            summa += product_item.price * item.amount
            product_item.quantity -= item.amount
            product_order.save()
            product_item.save()
            item.delete()
        serializer.save(
            user=user,
            cart=user.cart,
            total_sum=summa,
        )


        send_order.delay(user.email, serializer.data['id'])


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
