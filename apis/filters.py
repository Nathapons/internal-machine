from django_filters import FilterSet, filters

from apis.models import MachineIssue


class MachineIssueFilter(FilterSet):
    machine = filters.ModelChoiceFilter(queryset=MachineIssue.objects.all())
    title = filters.CharFilter(field_name='issue', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    start_timestamp = filters.DateFilter(field_name='timpstamp', lookup_expr='gte')
    end_timestamp = filters.DateFilter(field_name='timpstamp', lookup_expr='lte')
    status = filters.CharFilter(field_name='status', lookup_expr='iexact')

    class Meta:
        model = MachineIssue
        fields = ['machine', 'title', 'description', 'timestamp', 'status']
