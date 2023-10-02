from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apis.models import Machine
from apis.serializers import MachineCountSerializer


class MachineCountViewSet(ListModelMixin, GenericViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineCountSerializer
    pagination_class = None
