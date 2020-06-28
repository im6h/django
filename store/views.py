from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer, OrderSerializer, OrderDetailSerializer
from .models import Category, Product, Customer, Order, OrderDetail


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
  queryset = OrderDetail.objects.all()
  serializer_class = OrderDetailSerializer
