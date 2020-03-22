from rest_framework import serializers

from reestrdoma_app.models import Order


class OrderResource(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user.client.profile
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cad_num = validated_data.get('cad_num', instance.cad_num)
        instance.address = validated_data.get('address', instance.address)
        instance.square = validated_data.get('square', instance.square)
        instance.type = validated_data.get('type', instance.type)
        instance.xml_link = validated_data.get('xml_link', instance.xml_link)
        instance.zip_link = validated_data.get('zip_link', instance.zip_link)
        instance.html_link = validated_data.get('html_link', instance.html_link)
        instance.xml_link_status = validated_data.get('xml_link_status', instance.xml_link_status)
        instance.zip_link_status = validated_data.get('zip_link_status', instance.zip_link_status)
        instance.html_link_status = validated_data.get('html_link_status', instance.html_link_status)
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = '__all__'
