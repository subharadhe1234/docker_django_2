from django.urls import path,include
from . import views
from rest_framework import routers
urlpatterns=[
    path("",views.index,name="index"),
    path("a",views.data_request,name="Radhe"),
    path("rsa",views.encription,name="enctiption"),
    path("auth/",views.UserViewSet.as_view())
]
