from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from reestrdoma_app.models import Profile


class RegisterResource(serializers.Serializer):
    username = serializers.CharField(max_length=255, validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    password_confirmation = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=30)
    status = serializers.ChoiceField(choices=Profile.STATUSES)

    def validate(self, attrs):
        if attrs['password_confirmation'] != attrs['password']:
            raise ValidationError('Password not confirmed')
        return attrs

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        user = User()
        user.username = validated_data.get('username')
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.email = validated_data.get('email')
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class LoginResource(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UserResource(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
