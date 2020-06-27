from rest_framework import serializers
from .models import Hero, Power


class HeroSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Hero
    fields = '__all__'


class PowerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Power
    fields = '__all__'
    depth = 1
