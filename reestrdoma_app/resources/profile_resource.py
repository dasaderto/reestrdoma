from rest_framework import serializers

from reestrdoma_app.models import Profile


class ProfileResource(serializers.ModelSerializer):
    first_name = serializers.CharField(source='client.user.first_name')
    last_name = serializers.CharField(source='client.user.last_name')
    email = serializers.CharField(source='client.user.email')
    phone = serializers.CharField(source='client.phone')

    def update(self, instance, validated_data):
        instance.client.user.first_name = validated_data.get('client').get('user').get('first_name',
                                                                                       instance.client.user.first_name)
        instance.client.user.last_name = validated_data.get('client').get('user').get('last_name',
                                                                                      instance.client.user.last_name)
        instance.client.user.email = validated_data.get('client').get('user').get('email', instance.client.user.email)
        instance.client.phone = validated_data.get('client').get('phone', instance.client.phone)
        instance.status = validated_data.get('status', instance.status)
        instance.client.save()
        instance.client.user.save()
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['client']
