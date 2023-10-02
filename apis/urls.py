from django.urls import path, include
from rest_framework import routers

from apis.views import machine, machine_issue


routers = routers.DefaultRouter()
routers.register(r'machine', machine.MachineViewSet)
routers.register(r'machine-issue', machine_issue.MachineIssueViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]

