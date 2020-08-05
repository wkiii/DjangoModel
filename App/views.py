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
    4.在模型中(models.py中Person模型)创造了一个自定义的create类方法，然后用实例化后的对象执行save方法：Person.create()  peo.save()
    """

    flag = random.randrange(10000)
    # 方法一：
    # peo = Person()
    # peo.p_age = flag
    # peo.save()
    # 方法二：
    # #Person.objects.create(p_name="bob %d" % flag, p_age=15, p_sex=1)
    # 方法三：
    # ##peo = Person(p_name="Bob %d" % flag, p_age=15, p_sex=1)
    # ##peo.save()
    # 方法四：
    peo = Person.create(p_name="wurui")
    peo.save()
    return HttpResponse("add one")


def get_person(request):
    # 1.通过all()或者filter()方法获取到的是Queryset对象,但Queryset中的每个值都是模型对象；
    # # <QuerySet [<Person: Person object>, <Person: Person object>, ...]
    # 2.通过values()方法返回的也是一个Queryset对象，但Queryset中的每个值都是字典。
    # #  <QuerySet [{'id': 64, 'p_name': 'wurui', 'p_age': 100, 'p_sex': True, 'p_hobby': 'game'},...]
    # 3.values_list()方法返回的也是一个Queryset对象，但Queryset中的每个值都是一个不包含key只保留value的元祖。
    # # <QuerySet [(42, 'tom-0', 443590, False, None), (43, 'tom-1', 457126, False, None)...]
    pe1 = Person.objects.all()
    print(pe1)
    pe2 = pe1.values()
    print(pe2)
    pe3 = pe1.values_list()
    print(pe3)
    return render(request, "get_P.html", locals())
