from django.db import models
from django.utils import timezone
from team.models import Team

class Tweet(models.Model):
    date = models.DateTimeField(
        default=timezone.now)
    text = models.CharField(
        max_length=140)
    latitude = models.FloatField()
    longitude = models.FloatField()
    team = models.ForeignKey(
        'team.Team',
        on_delete=models.CASCADE,
    )
    score = models.IntegerField()
    def __str__(self):
        return self.text
