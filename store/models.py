# Create your models here.

from django.db import models

# Categories


class Category(models.Model):
  cate_name = models.CharField(max_length=200)
  cate_description = models.TextField()

  def __str__(self):
    return self.cate_name

# Products


class Product(models.Model):
  pro_name = models.CharField(max_length=200)
  pro_cate = models.ForeignKey(Category, on_delete=models.CASCADE)
  pro_descripton = models.TextField()
  pro_price = models.IntegerField(default=0)
  pro_active = models.BooleanField(default=True)

  def __str__(self):
    return self.pro_name

# Customers


class Customer(models.Model):
  cus_name = models.CharField(max_length=200)
  cus_phone = models.CharField(max_length=200)
  cus_address = models.CharField(max_length=200)
  cus_username = models.CharField(max_length=50)
  cus_password = models.CharField(max_length=16)
  cus_email = models.EmailField()

  def __str__(self):
    return self.cus_name


# Order


class Order(models.Model):
  cus_id = models.ForeignKey(
      Customer, on_delete=models.SET_NULL, null=True, blank=True)
  ord_date = models.DateTimeField(auto_now_add=True)
  ord_price = models.IntegerField(default=0)

# Order detail


class OrderDetail(models.Model):
  ord_id = models.ForeignKey(Order, on_delete=models.CASCADE)
  pro_id = models.ForeignKey(
      Product, on_delete=models.SET_NULL, null=True, blank=True)
  ord_price = models.IntegerField(default=0)
  ord_quanlity = models.IntegerField(default=1)
  ord_discount = models.IntegerField(default=0)
