from django.urls import path, include
from rest_framework import routers

from apis.views import machine, machine_filter, machine_issue, machine_issue_report


routers = routers.DefaultRouter()
routers.register(r'machine', machine.MachineViewSet)
routers.register(r'machine-issue', machine_issue.MachineIssueViewSet)
routers.register(r'machine-issue-report', machine_issue_report.MachineIssueReportViewSet)
routers.register(r'machine-issue-filter', machine_filter.MachineFilterViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]

