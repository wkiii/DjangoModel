from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^getuser/', views.getuser),
    url(r'^adduser/', views.adduser),
]
