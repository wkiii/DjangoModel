import random

from django.db.models import Avg, Max, Min, Sum, F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import User, Order, Grade, Students, Company, Animal


def login(request):
    username = "hehe1620"
    password = "1620"
    users = User.objects.filter(username=username)
    if users.exists():
        user = users.first()
        if user.password == password:
            he = "login success!"
        else:
            he = "password Wrong!"
    else:
        he = "username is not exist!"
    return HttpResponse(he)


def adduser(request):
    flag = random.randrange(10000)
    User.objects.create(username="hehe%s" % flag, password=flag)
    return HttpResponse("add user: hehe%s" % flag)


def getuser(request):
    # users = User.objects.all()[2:10]
    return render(request, "getuser.html", locals())


def getorder(request):
    orders = Order.objects.filter(o_time__month=6)
    for i in orders:
        print(i.num)
    return HttpResponse("订单获取成功")


def getstudents(request):
    grade = Grade.objects.filter(students__s_name="tom")
    for g in grade:
        print(g.g_name)
    stu = Students.objects.filter()
    for s in stu:
        print(s.s_name)
    grade = Grade.objects.get(g_name='linux')
    stu = grade.students_set.all()
    print("ffffffffffffffffff")
    for i in stu:
        print(i.s_name)
    return HttpResponse("hehe")


def getbill(request):
    s_bill = Students.objects.aggregate(Sum("bill"))
    p_bill = Students.objects.aggregate(Max("bill"))
    k_bill = Students.objects.aggregate(Avg("bill"))
    g_bill = Students.objects.aggregate(Min("bill"))
    print(s_bill, p_bill, k_bill, g_bill)
    return HttpResponse("get bill ok.")


def getcompany(request):
    company1 = Company.objects.filter(girls_num__lt=F('boys_num'))
    for i in company1:
        print(i.c_name)
    company2 = Company.objects.filter(Q(girls_num__lt=F('boys_num')) & Q(boys_num=89))
    for j in company2:
        print(j.c_name)
    return HttpResponse("get Company")


def getanimal(request):
    animal = Animal.objects.all()
    for i in animal:
        print(i.name)
    return HttpResponse("animal got it!")