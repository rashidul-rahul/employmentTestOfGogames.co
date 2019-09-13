from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GameSerializer
from .models import Game
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet


class CategoryFilterSet(FilterSet):
    class Meta:
        model = Game
        fields = ('category_id',)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CategoryFilterSet