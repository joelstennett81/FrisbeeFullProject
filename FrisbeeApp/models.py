from django.db import models

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
    game = models.ForeignKey('TeamGame', on_delete=models.CASCADE, default='')
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    turnovers = models.PositiveIntegerField(default=0)
    completions = models.PositiveIntegerField(default=0)
    throwaways = models.PositiveIntegerField(default=0)
    drops = models.PositiveIntegerField(default=0)
    passing_yards = models.IntegerField(default=0)
    receiving_yards = models.IntegerField(default=0)
    touches = models.PositiveIntegerField(default=0)

class PlayerSeason(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, default='')
    league_season = models.ForeignKey('LeagueSeason', on_delete=models.CASCADE, default='')
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

class League(models.Model):
    name = models.CharField(max_length = 100)
    team_one = models.ForeignKey('Team', related_name='league_team_one', on_delete=models.CASCADE, default='')
    team_two = models.ForeignKey('Team', related_name='league_team_two', on_delete=models.CASCADE, default='')
    team_three = models.ForeignKey('Team', related_name='league_team_three', on_delete=models.CASCADE, default='')
    team_four = models.ForeignKey('Team', related_name='league_team_four', on_delete=models.CASCADE, default='')
    team_five = models.ForeignKey('Team', related_name='league_team_five', on_delete=models.CASCADE, default='')
    team_six = models.ForeignKey('Team', related_name='league_team_six', on_delete=models.CASCADE, default='')
    team_seven = models.ForeignKey('Team', related_name='league_team_seven', on_delete=models.CASCADE, default='')
    team_eight = models.ForeignKey('Team', related_name='league_team_eight', on_delete=models.CASCADE, default='')
    team_nine = models.ForeignKey('Team', related_name='league_team_nine', on_delete=models.CASCADE, default='')
    team_ten = models.ForeignKey('Team', related_name='league_team_ten', on_delete=models.CASCADE, default='')

class LeagueSeason(models.Model):
    name = models.CharField(max_length = 100) 
    year = models.DateField()
    league = models.ForeignKey('League', on_delete=models.CASCADE, default='')

class SeasonGame(models.Model):
    league_season = models.ForeignKey('LeagueSeason', on_delete=models.CASCADE, default='')
    team_one = models.ForeignKey('Team', related_name='season_game_team_one', on_delete=models.CASCADE, default='')
    team_two = models.ForeignKey('Team', related_name='season_game_team_two', on_delete=models.CASCADE, default='')
    team_one_score = models.IntegerField(default=0)
    team_two_score = models.IntegerField(default=0)
    winner = models.ForeignKey('Team', related_name='season_game_winner' ,on_delete=models.CASCADE, default='')
    loser = models.ForeignKey('Team', related_name='season_game_loser', on_delete=models.CASCADE, default='')

class TeamGame(models.Model):
    league_season = models.ForeignKey('LeagueSeason', on_delete=models.CASCADE, default='')
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    throwaways = models.IntegerField(default=0)
    drops = models.IntegerField(default=0)
    breaks = models.IntegerField(default=0)

