from rest_framework import serializers
from main.models import Visit
from main.utils import ValidatorSerializer


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('id', 'shop', 'longitude', 'latitude')


class VisitsFilterSerializer(ValidatorSerializer):
    phone = serializers.CharField()
