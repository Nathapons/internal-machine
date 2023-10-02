from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from apis.models import MachineIssue
from apis.serializers import MachineHistorySerializer


class MachineHistoryViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = MachineIssue.objects.all()
    serializer_class = MachineHistorySerializer
    