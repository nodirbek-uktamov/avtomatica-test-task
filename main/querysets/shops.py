from django.db.models import QuerySet


class ShopsQuerySet(QuerySet):
    def list(self, phone):
        query = self.filter(worker__phone_number=phone) if phone else self
        return query
