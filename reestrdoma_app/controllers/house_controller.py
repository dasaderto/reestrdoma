from django.http import JsonResponse
from rest_framework.views import APIView

from reestrdoma_app.models import House
from reestrdoma_app.resources.house_resource import HouseResource


class HouseView(APIView):
    def get(self, *args, **kwargs):
        is_all_houses = 'houseId' not in self.request.GET
        if is_all_houses:
            houses = House.objects.all()
        else:
            houses = House.objects.get(pk=self.request.GET.get('houseId'))

        return JsonResponse({
            'success': True,
            'data': HouseResource(houses, many=is_all_houses).data
        })

    def post(self, request):
        data = HouseResource(data=request.POST, context={'request': request})

        if not data.is_valid():
            return JsonResponse({
                'success': False,
                'data': data.errors
            }, status=400)

        new_house = data.create(validated_data=data.validated_data)

        return JsonResponse({
            'success': True,
            'data': HouseResource(new_house).data
        })

    def put(self, *args, **kwargs):

        if 'houseId' not in self.request.GET:
            return JsonResponse({
                'success': False,
                'data': 'house id is undefined'
            }, status=404)

        house_id = self.request.GET.get('houseId')
        house = House.objects.filter(id=house_id).first()
        if not house:
            return JsonResponse({
                'success': False,
                'data': 'house with this id is undefined'
            }, status=404)

        data = HouseResource(data=self.request.POST)
        if not data.is_valid():
            return JsonResponse({
                'success': False,
                'data': data.errors
            }, status=400)

        updated_house = data.update(instance=house, validated_data=data.validated_data)

        return JsonResponse({
            'success': True,
            'data': HouseResource(updated_house).data
        })
