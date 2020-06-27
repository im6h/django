from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import HeroSerializer, PowerSerializer
from .models import Hero, Power


class HeroViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Hero.objects.all()
  serializer_class = HeroSerializer


class PowerViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Power.objects.all()
  serializer_class = PowerSerializer
