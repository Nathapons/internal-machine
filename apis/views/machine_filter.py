from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apis.models import MachineIssue
from apis.filters import MachineIssueFilter
from apis.serializers import MachineIssueReportSerializer


class MachineFilterViewSet(ListModelMixin, GenericViewSet):
    queryset = MachineIssue.objects.all()
    serializer_class = MachineIssueReportSerializer
    filterset_class = MachineIssueFilter
    pagination_class = None
