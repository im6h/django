from django.db import models

# Create your models here.


class Hero(models.Model):
  name = models.CharField(max_length=60)
  alias = models.CharField(max_length=60)

  def __str__(self):
    return self.name


class Power(models.Model):
  hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
  power = models.CharField(max_length=200)
  rate = models.IntegerField(default=0)
