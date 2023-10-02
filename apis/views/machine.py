from rest_framework.viewsets import ModelViewSet

from apis.models import Machine
from apis.serializers import MachineSerializer


class MachineViewSet(ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    pagination_class = None
