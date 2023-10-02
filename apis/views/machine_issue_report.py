from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apis.models import MachineIssue
from apis.serializers import MachineIssueReportSerializer


class MachineIssueReportViewSet(ListModelMixin, GenericViewSet):
    queryset = MachineIssue.objects.all()
    serializer_class = MachineIssueReportSerializer
