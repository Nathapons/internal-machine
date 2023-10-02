from django.urls import path, include
from rest_framework import routers

from apis.views import machine


routers = routers.DefaultRouter()
routers.register(r'machine', machine.MachineViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]

