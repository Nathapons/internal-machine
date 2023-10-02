from django.urls import path, include
from rest_framework import routers

from apis.views import machine, machine_filter, machine_issue, machine_issue_report, \
    machine_count, machine_common


routers = routers.DefaultRouter()
routers.register(r'machine', machine.MachineViewSet)
routers.register(r'machine-issue', machine_issue.MachineIssueViewSet)
routers.register(r'machine-issue-report', machine_issue_report.MachineIssueReportViewSet)
routers.register(r'machine-issue-filter', machine_filter.MachineFilterViewSet)
routers.register(r'machine-count', machine_count.MachineCountViewSet)
routers.register(r'machine-common', machine_common.MachineCommonViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]

