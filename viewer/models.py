from django.db import models
from accounts.models import Users


# Create your models here.


class Teams(models.Model):
    team_name = models.CharField(max_length=100)
    manager = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.team_name


class TeamMembers(models.Model):
    team_name = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)
    member_name = models.ManyToManyField(Users)


class Tasks(models.Model):
    task_name = models.CharField(max_length=360)
    team_name = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)
    member_name = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    plan_end_date = models.DateField()
    actual_end_date = models.DateField(null=True)

    def __str__(self):
        return self.task_name
