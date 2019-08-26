import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Person


def add_persons(request):
    """一次性新增了多个数据库字段。"""
    for i in range(15):
        peo = Person()
        flag = random.randrange(1000000)
        peo.p_name = "tom-%d" % i
        peo.p_age = flag
        peo.p_sex = flag % 2
        peo.save()
    return render(request, "add_PS.html")


def add_person(request):
    """
    ##一次性新增一个数据库字段的三种方式：
    1.先实例化对象，然后依次或者随意给类属性赋值(没有赋值的属性，默认保存为blank)，最后执行对象的save方法；
    2.直接用类的方法，但create方法内部需要填写所有字段； Person.objects.create()
    3.将类实例化的过程中，直接在类中赋值属性(赋值所有属性)，然后用实例化对象的save方法：peo = Person()   peo.save()
    """
    # save的方式，可以填写任意字段，任意字段都可以为空(需要注意unique的字段只能空白一次)
    # Person.objects.create()这种方式，括号内必须填写所有字段；
    # Person() 这种方式同上，括号内也是填写所有字段。

    flag = random.randrange(10000)
    # peo = Person()
    # peo.p_age = flag
    # peo.save()
    # #Person.objects.create(p_name="bob %d" % flag, p_age=15, p_sex=1)
    peo = Person(p_name="Bob %d" % flag)
    peo.save()
    return HttpResponse("add one")


def get_person(request):
    pe1 = Person.objects.all()
    return render(request, "get_P.html", locals())
