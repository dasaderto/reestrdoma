from rest_framework import serializers

from reestrdoma_app.models import Profile


class ProfileResource(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone = serializers.CharField(source='user.phone')

    def update(self, instance, validated_data):
        instance.user.first_name = validated_data.get('user').get('first_name',
                                                                  instance.user.first_name)
        instance.user.last_name = validated_data.get('user').get('last_name',
                                                                 instance.user.last_name)
        instance.user.email = validated_data.get('user').get('email', instance.user.email)
        instance.user.phone = validated_data.get('user').get('phone', instance.user.phone)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        instance.user.save()
        return instance

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']
