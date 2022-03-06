from rest_framework.serializers import Serializer


def pagination(queryset, serializer, page, size=15):
    serializer.instance = pagination_queryset(queryset, page, size)['queryset']
    return {'count': queryset.count(), 'results': serializer.data}


def pagination_queryset(queryset, page, size=15):
    page = page or 1
    offset = (page - 1) * size
    limit = offset + size
    return {'queryset': queryset[offset:limit], 'limit': limit, 'offset': offset}


class ValidatorSerializer(Serializer, object):
    class BaseSerializer(Serializer):
        def update(self, instance, validated_data):
            pass

        def create(self, validated_data):
            pass

    @classmethod
    def check(cls, data, many=False, context=None):
        serializer = cls(data=data, many=many, context=context or {})
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
