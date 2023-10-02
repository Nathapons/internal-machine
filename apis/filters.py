from django_filters import FilterSet, filters

from apis.models import MachineIssue, Machine
from apis.choices import MACHINE_ISSUE_STATUS


class MachineIssueFilter(FilterSet):
    machine = filters.ModelChoiceFilter(queryset=Machine.objects.all())
    title = filters.CharFilter(field_name='issue', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    start_timestamp = filters.DateFilter(field_name='timpstamp', lookup_expr='gte')
    end_timestamp = filters.DateFilter(field_name='timpstamp', lookup_expr='lte')
    status = filters.MultipleChoiceField(choices=MACHINE_ISSUE_STATUS)

    class Meta:
        model = MachineIssue
        fields = ['machine', 'title', 'description', 'start_timestamp', 'end_timestamp', 'status']
        