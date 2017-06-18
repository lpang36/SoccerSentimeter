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
    homeColourRed = models.IntegerField()
    homeColourBlue = models.IntegerField()
    homeColourGreen = models.IntegerField()
    awayColourRed = models.IntegerField()
    awayColourBlue = models.IntegerField()
    awayColourGreen = models.IntegerField()
    league = models.CharField(
        max_length = 30)
    nextGame = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.longName
"""
class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
"""
class Player(models.Model):
    name = models.CharField(
        max_length=50)
    score = models.IntegerField()
    lastScore = models.IntegerField()
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
    )
