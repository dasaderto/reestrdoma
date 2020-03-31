from functools import wraps
from hashlib import md5

from django.http import JsonResponse


def check_api_token(function):
    @wraps(function)
    def decorator(self, request, *args, **kwargs):
        if ('api_token' in request.GET.keys()) and (request.GET.get('api_token') == md5(b'ReestrDoma').hexdigest()):
            return function(self, request, *args, **kwargs)
        else:
            return JsonResponse({
                'success': False,
                'data': {
                    'api_token': ['api_token is invalid']
                }
            })

    return decorator
