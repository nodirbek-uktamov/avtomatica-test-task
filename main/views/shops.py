
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Shop
from main.serializers.shops import ShopsSerializer, ShopsFilterSerializer
from main.utils import pagination


class ShopsListView(APIView):
    def get(self, request):
        params = ShopsFilterSerializer.check(request.GET)
        queryset = Shop.objects.list(phone=params.get('phone'))
        serializer = ShopsSerializer(many=True)
        data = pagination(queryset, serializer, params.get('page'))
        return Response(data)
