from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    objects = models.Manager()


class Order(models.Model):
    num = models.CharField(max_length=16, unique=True)
    o_time = models.DateTimeField(auto_now_add=True)


class Grade(models.Model):
    g_name = models.CharField(max_length=32, unique=True)
    objects = models.Manager()


class Students(models.Model):
    s_name = models.CharField(max_length=32)
    s_grade = models.ForeignKey(Grade)
    bill = models.IntegerField(default=1000)
    objects = models.Manager()


class Company(models.Model):
    c_name = models.CharField(max_length=32)
    girls_num = models.IntegerField()
    boys_num = models.IntegerField()


class AnimalManager(models.Manager):
    def get_queryset(self):
        return super(AnimalManager, self).get_queryset().filter(is_delete=False)


class Animal(models.Model):
    name = models.CharField(max_length=32)
    is_delete = models.BooleanField(default=False)
    # objects = models.Manager()
    objects = AnimalManager()
