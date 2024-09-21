from django.urls import path,include
from . import views
from .views import GroupViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', GroupViewSet, basename='group') 
urlpatterns=[
    path("",views.index,name="index"),
    path("a",views.data_request,name="Radhe"),
    path("rsa",views.encription,name="enctiption"),
    # path("auth/",views.UserViewSet.as_view(),name="userview"),
    path('auth/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('groups/<int:pk>/', GroupViewSet.as_view({'get': 'retrieve'}), name='group-detail'),

]
