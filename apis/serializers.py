from rest_framework import serializers

from apis.models import Machine, MachineIssue


class MachineSerializer(serializers.ModelSerializer):

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

    @staticmethod
    def get_issue_count(machine):
        return machine.machine_machine_issue.count()

    class Meta:
        model = Machine
        fields = ['machine_id', 'issue_count']


class MachineCommonSerializer(serializers.ModelSerializer):
    word = serializers.CharField(source='issue')
    frequency = serializers.SerializerMethodField()

    @staticmethod
    def get_frequency(machine_issue):
        return MachineIssue.objects.filter(issue=machine_issue.issue).count()

    class Meta:
        model = MachineIssue
        fields = ['word', 'frequency']


class MachineHistorySerializer(serializers.ModelSerializer):
    comment = serializers.CharField(max_length=255, write_only=True)

    machine = serializers.IntegerField(source='machine.id', read_only=True)
    issue = serializers.CharField(max_length=255, read_only=True)
    description = serializers.CharField(max_length=255, read_only=True)
    history = serializers.SerializerMethodField()

    def get_history(self, machine_issue):
        machine_issues = MachineIssue.objects.filter(machine=machine_issue.machine).order_by('timestamp')
        return machine_issues.values('status', 'timestamp')
    
    def update(self, machine_issue, validated_data):
        machine_issue.id = None

        machine_issue.status = validated_data['status']
        machine_issue.description = validated_data['comment']
        machine_issue.save()

        return machine_issue

    class Meta:
        model = MachineIssue
        fields = ['id', 'machine', 'issue', 'description', 'timestamp', 'status', 'history', 'comment']
