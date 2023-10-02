from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from apis.models import MachineIssue
from apis.serializers import MachineIssueSerializer, MachineIssueReportSerializer


class MachineIssueViewSet(ModelViewSet):
    queryset = MachineIssue.objects.all()
    serializer_class = MachineIssueSerializer
    pagination_class = None
