
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'teams'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)  # Store team name for simplicity
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    user_email = models.EmailField()  # Store user email for simplicity
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()
    def __str__(self):
        return f"{self.user_email} - {self.type}"
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.JSONField(default=list)  # List of team names
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100, unique=True)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team}: {self.points}"
    class Meta:
        db_table = 'leaderboard'
