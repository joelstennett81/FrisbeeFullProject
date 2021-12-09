from django.db import models

class Game(models.Model):
    teamOne = models.ForeignKey('Team', related_name='teamOne', on_delete=models.CASCADE)
    teamTwo = models.ForeignKey('Team', related_name='teamTwo', on_delete=models.CASCADE)
    windspeed = models.PositiveIntegerField()

class League(models.Model):
    name = models.CharField(max_length = 100)

class Player(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    jersey_number = models.IntegerField()
    overall_rating = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    is_handle = models.BooleanField()
    is_cutter = models.BooleanField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE, default='')

class PlayerGame(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, default='')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, default='')
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    turnovers = models.PositiveIntegerField(default=0)
    completions = models.PositiveIntegerField(default=0)
    throwaways = models.PositiveIntegerField(default=0)
    drops = models.PositiveIntegerField(default=0)
    passing_yards = models.IntegerField(default=0)
    receiving_yards = models.IntegerField(default=0)
    touches = models.PositiveIntegerField(default=0)

class Team(models.Model):
    city = models.CharField(max_length = 50)
    mascot = models.CharField(max_length = 50)
    overall_rating = models.IntegerField()
    league = models.ForeignKey('League', on_delete=models.CASCADE)
