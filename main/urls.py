from django.urls import path

from main.views import shops, visits

urlpatterns = [
    path('shops/', shops.ShopsListView.as_view(), name='shops-list'),
    path('visit/', visits.VisitView.as_view(), name='visit'),
]
