from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from main.serializers.visits import VisitSerializer, VisitsFilterSerializer


class VisitView(APIView):
    def post(self, request):
        params = VisitsFilterSerializer.check(request.GET)
        serializer = VisitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if data.get('shop').worker.phone_number != params.get('phone'):
            raise ValidationError({'message': 'Доступ запрещен', 'ok': False})  # or some other auth error

        serializer.save()
        return Response(serializer.data, 201)
