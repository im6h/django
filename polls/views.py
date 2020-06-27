from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer, PowerSerializer
from .models import Hero, Power


class HeroViewSet(viewsets.ModelViewSet):
  queryset = Hero.objects.all()
  serializer_class = HeroSerializer


class PowerViewSet(viewsets.ModelViewSet):
  queryset = Power.objects.all()
  serializer_class = PowerSerializer
