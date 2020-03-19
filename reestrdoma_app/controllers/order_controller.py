from django.http import JsonResponse
from rest_framework.views import APIView

from reestrdoma_app.models import Order
from reestrdoma_app.resources.order_resource import OrderResource


class OrderView(APIView):
    def get(self, *args, **kwargs):
        if 'houseId' not in self.request.GET:
            return JsonResponse({
                'success': False,
                'data': ['houseId is undefined']
            })

        house_id = self.request.GET.get('houseId')
        orders = Order.objects.filter(house=house_id)

        return JsonResponse({
            'success': True,
            'data': OrderResource(orders, many=True).data
        })

    def post(self, *args, **kwargs):
        data = OrderResource(data=self.request.POST)

        if not data.is_valid():
            return JsonResponse({
                'success': False,
                'data': data.errors
            }, status=400)

        new_order = data.create(validated_data=data.validated_data)

        return JsonResponse({
            'success': True,
            'data': OrderResource(new_order).data
        })

    def put(self, *args, **kwargs):
        if 'orderId' not in self.request.GET:
            return JsonResponse({
                'success': False,
                'data': ['house id is undefined']
            })

        order_id = self.request.GET.get('orderId')
        order = Order.objects.get(pk=order_id)

        data = OrderResource(data=self.request.POST)
        if not data.is_valid():
            return JsonResponse({
                'success': False,
                'data': data.errors
            }, status=400)

        updated_order = data.update(instance=order, validated_data=data.validated_data)

        return JsonResponse({
            'success': True,
            'data': OrderResource(updated_order).data
        })
