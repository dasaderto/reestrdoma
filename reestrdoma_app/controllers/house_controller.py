from django.http import JsonResponse
from rest_framework.views import APIView

from reestrdoma_app.models import House
from reestrdoma_app.resources.house_resource import HouseResource


class HouseView(APIView):
    def get(self):
        is_all_houses = 'houseId' not in self.request.GET
        if is_all_houses:
            houses = House.objects.all()
        else:
            houses = House.objects.get(pk=self.request.GET.get('houseId'))

        return JsonResponse({
            'success': True,
            'data': HouseResource(houses, many=is_all_houses).data
        })

    def post(self):
        data = HouseResource(data=self.request.GET)

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

    def put(self):

        if 'houseId' not in self.request.GET:
            return JsonResponse({
                'success': False,
                'data': ['house id is undefined']
            })

        house_id = self.request.GET.get('houseId')
        house = House.objects.get(pk=house_id)

        data = HouseResource(data=self.request.GET)
        if not data.is_valid():
            return JsonResponse({
                'success': False,
                'data': data.errors
            }, status=400)

        updated_house = data.update(instance=house,validated_data=data.validated_data)

        return JsonResponse({
            'success': True,
            'data': HouseResource(updated_house).data
        })
