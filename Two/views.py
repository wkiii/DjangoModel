import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import User


def getuser(request):
    username = "hehe11620"
    password = "1620123"
    users = User.objects.filter(username=username)
    if users.exists():
        user = users.first()
        if user.password == password:
            print("login success!")
        else:
            print("password Wrong!")
    else:
        print("username is not exist!")
    return HttpResponse("hehe")


def adduser(request):
    flag = random.randrange(10000)
    User.objects.create(username="hehe%s" % flag, password=flag)
    return HttpResponse("add user: hehe%s" % flag)
