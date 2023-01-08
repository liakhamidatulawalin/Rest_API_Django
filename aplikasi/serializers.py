from rest_framework import serializers
from aplikasi.models import ItemsModel


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = ['name', 'price']
