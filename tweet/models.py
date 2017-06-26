from django.db import models
from django.utils import timezone
from team.models import Team

class Tweet(models.Model):
    date = models.DateTimeField(
        default=timezone.now,)
    link = models.CharField(
        max_length=25)
    latitude = models.FloatField(
		null=True)
    longitude = models.FloatField(
		null=True)
    team = models.ForeignKey(
        'team.Team',
        on_delete=models.CASCADE,
    )
    score = models.IntegerField(
        default=0)
    def __str__(self):
        return self.link
