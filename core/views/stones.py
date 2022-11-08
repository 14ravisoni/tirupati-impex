from rest_framework import viewsets, filters

from core.models import Stone, StoneJadaiTransaction
from core.serializers import StoneSerializer


class StoneViewSet(viewsets.ModelViewSet):
    queryset = Stone.objects.all()
    serializer_class = StoneSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['stone_name']


class StoneJadaiTransactionViewSet(viewsets.ModelViewSet):
    queryset = StoneJadaiTransaction.objects.all()
    serializer_class = StoneJadaiTransaction
    filter_backends = [filters.SearchFilter]
    search_fields = ['jewl']
