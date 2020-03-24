from rest_framework import serializers

from reestrdoma_app.models import House


class HouseResource(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.flat_count = validated_data.get('flat_count', instance.flat_count)
        instance.actual_date = validated_data.get('actual_date', instance.actual_date)
        instance.reestr_link = validated_data.get('reestr_link', instance.reestr_link)
        instance.status = validated_data.get('status', instance.status)
        instance.square = validated_data.get('square', instance.square)
        instance.rights = validated_data.get('rights', instance.rights)
        instance.save()
        return instance

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return House.objects.create(**validated_data)

    class Meta:
        model = House
        fields = '__all__'
