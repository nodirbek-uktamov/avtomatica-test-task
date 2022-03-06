from rest_framework import serializers
from main.models import Shop
from main.utils import ValidatorSerializer


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name',)


class ShopsFilterSerializer(ValidatorSerializer):
    phone = serializers.CharField()
    page = serializers.IntegerField(default=1, required=False)
