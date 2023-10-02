from rest_framework import serializers

from apis.models import Machine, MachineIssue


class MachineSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Machine
        fields = '__all__'


class MachineIssueSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {'machine_id': instance.machine.id, 'issue': instance.issue, 'description': instance.description}

    class Meta:
        model = MachineIssue
        fields = '__all__'



class MachineIssueReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = MachineIssue
        fields = ['id', 'machine', 'issue', 'description', 'timestamp', 'status']


class MachineCountSerializer(serializers.ModelSerializer):
    machine_id = serializers.IntegerField(source='id')
    issue_count = serializers.SerializerMethodField()

    def get_issue_count(self, machine):
        return machine.machine_machine_issue.count()

    class Meta:
        model = Machine
        fields = ['machine_id', 'issue_count']
