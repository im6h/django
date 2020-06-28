from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderDetail
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(OrderDetail)
admin.site.register(Order)
