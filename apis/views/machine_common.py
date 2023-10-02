from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apis.models import MachineIssue
from apis.serializers import MachineCommonSerializer


class MachineCommonViewSet(ListModelMixin, GenericViewSet):
    queryset = MachineIssue.objects.distinct('issue')
    serializer_class = MachineCommonSerializer
    pagination_class = None
