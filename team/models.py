from django.db import models
from django.utils import timezone
from django.core.validators import *

class Team(models.Model):
    date = models.DateField(
        default=timezone.now)
    publishedDate = models.DateTimeField(
        default=timezone.now)
    score = models.IntegerField()
    scoreList = models.CharField(
        max_length=500,
        validators=[validate_comma_separated_integer_list],
    )
    associatedTags = models.TextField()
    name = models.CharField(
        max_length = 5)
    longName = models.CharField(
        max_length = 30)
    homeColour = models.CharField(
		max_length = 6,
		null=True,
	)
    awayColour = models.CharField(
		max_length = 6,
		null=True,
	)
    league = models.CharField(
        max_length = 30)
    nextGame = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        null=True,
    )
    def __str__(self):
        return self.longName
    
class Player(models.Model):
    name = models.CharField(
        max_length=50)
    score = models.IntegerField()
    lastScore = models.IntegerField()
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
    )
