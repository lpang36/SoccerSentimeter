from django.db import models
from django.utils import timezone
from team.models import Team

class Game(models.Model):
    team1 = models.ForeignKey(
        'team.Team',
        on_delete=models.CASCADE,
        related_name='1+',
    )
    team2 = models.ForeignKey(
        'team.Team',
        on_delete=models.CASCADE,
        related_name='2+',
    )
