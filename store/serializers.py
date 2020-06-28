from rest_framework import serializers
from .models import Category, Product, Customer, Order, OrderDetail


class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'
    depth = 1


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Customer
    fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'
    depth = 1


class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = OrderDetail
    fields = '__all__'
    depth = 3
