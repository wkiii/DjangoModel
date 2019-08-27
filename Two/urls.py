from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^adduser/', views.adduser),
    url(r'^getuser/', views.getuser),
    url(r'^getorder/', views.getorder),
    url(r'^getstudents/', views.getstudents),
    url(r'^getbill/', views.getbill),
    url(r'^getcompany/', views.getcompany),
    url(r'^getanimal/', views.getanimal),
]
