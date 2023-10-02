from rest_framework import serializers

from apis.models import Machine


class MachineSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Machine
        fields = '__all__'
