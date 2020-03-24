from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView

from reestrdoma_app.models import Profile, get_tokens_for_user
from reestrdoma_app.resources.profile_resource import ProfileResource
from reestrdoma_app.resources.user_resource import RegisterResource, LoginResource
from reestrdoma_app.services.register_service import RegisterService


class ProfileView(APIView):
    def put(self, *args, **kwargs):
        data = ProfileResource(data=self.request.POST)

        if not data.is_valid():
            return JsonResponse({
                'success': False,
                'data': data.errors
            }, status=400)

        profile = Profile.objects.get(user=self.request.user.id)
        updated = data.update(instance=profile, validated_data=data.validated_data)

        return JsonResponse({
            'success': True,
            'data': ProfileResource(updated).data
        })


class RegisterView(APIView):
    def post(self, *args, **kwargs):
        data = RegisterResource(data=self.request.POST)

        if not data.is_valid():
            return JsonResponse({
                'success': False,
                'data': data.errors
            })

        service = RegisterService()

        user = service.make(data)
        if not user:
            raise Exception('Something wrong')

        token = get_tokens_for_user(user)

        return JsonResponse({
            'success': True,
            'data': {
                'user': ProfileResource(user.profile).data,
                'token': token
            }
        })


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        data = LoginResource(data=self.request.POST)

        if not data.is_valid():
            return JsonResponse({
                'success': False,
                'data':  data.errors
            }, status=400)

        user = authenticate(username=data.validated_data.get('username'), password=data.validated_data.get('password'))
        if user is None:
            return JsonResponse({
                'success': False,
                'data': 'User not found'
            }, status=400)

        token = get_tokens_for_user(user)

        return JsonResponse({
            'success': True,
            'data': {
                'user': ProfileResource(user.profile).data,
                'token': token
            }
        })
