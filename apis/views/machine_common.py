from drf_yasg.utils import swagger_auto_schema

from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from apis.models import MachineIssue
from apis.serializers import MachineCommonSerializer
from apis.schemas import top_k_params


class MachineCommonViewSet(ListModelMixin, GenericViewSet):
    queryset = MachineIssue.objects.distinct('issue')
    serializer_class = MachineCommonSerializer
    pagination_class = None

    @swagger_auto_schema(manual_parameters=[top_k_params])
    def list(self, request, *args, **kwargs):
        top_k = int(request.query_params.get('top_k', 5))

        data = self.get_serializer(self.get_queryset(), many=True).data
        data = sorted(data, key=lambda d: d['frequency'], reverse=True)[:top_k]
        
        return Response(data, status=status.HTTP_200_OK)
