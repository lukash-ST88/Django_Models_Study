from django.db import models
from datetime import date
from django.utils import timezone

class Game(models.Model):
    team = models.CharField(max_length=30)
    city = models.CharField(max_length=30, default=team, null=True)
    g_scored = models.SmallIntegerField(null=True)
    g_conceded = models.SmallIntegerField(null=True)
    game_date = models.DateField(default=timezone.now)
    participants = models.ManyToManyField('Player', through='Lineup')

    def __str__(self):
        return self.team

class Player(models.Model):
    pos = [('GK', 'Goalkeeeper'), ('DF', 'Defender'), ('MD', 'Midfielder'), ('FW', 'Forward'),]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=20)
    number = models.IntegerField()
    positon = models.CharField(max_length=2, choices=pos)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Lineup(models.Model):
    IN_START = [('IN', 'IN start'), ('OUT', 'IN reserve')]
    CARDS = [('Y', 'Yellow'), ('Y2', 'Two yellow cards'), ('R', 'Straight red'), ('YR', 'Yellow + Straight red'), ('NUll', 'No cards')]
    start = models.CharField(max_length=3, choices=IN_START)
    time_in = models.FloatField()
    goals = models.SmallIntegerField(null=True)
    card = models.CharField(max_length=4, choices=CARDS)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)










