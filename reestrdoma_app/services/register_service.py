from reestrdoma_app.models import User
from reestrdoma_app.resources.user_resource import RegisterResource


class RegisterService:
    def make(self, data: RegisterResource) -> User:
        valided_data = data.validated_data

        user = data.create(validated_data=valided_data)

        user.phone = valided_data.get('phone')
        user.save()

        user.profile.status = valided_data.get('status')
        user.profile.save()

        return user
