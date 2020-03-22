from django.contrib.auth.models import User

from reestrdoma_app.resources.user_resource import RegisterResource


class RegisterService:
    def make(self, data: RegisterResource) -> User:
        valided_data = data.validated_data

        user = data.create(validated_data=valided_data)

        user.client.phone = valided_data.get('phone')
        user.client.save()

        user.client.profile.status = valided_data.get('status')
        user.client.profile.save()

        return user
