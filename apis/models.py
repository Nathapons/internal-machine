from django.db import models

from . import choices

# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.id} machine name: {self.name}'


class MachineIssue(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='machine_machine_issue')
    issue = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    timestamp = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=choices.MACHINE_ISSUE_STATUS)

    def __str__(self):
        return f'id: {self.id}, machine: {self.machine.name}, status: {self.status}'



