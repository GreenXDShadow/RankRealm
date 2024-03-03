from django.contrib.auth.models import User  # Import Django's built-in User model
from django.db import models  # Import Django's model module to define model fields and behavior
from django.utils.translation import gettext_lazy as _  # Import for text translation (used in Role Iterator)

"""
    This file contains essentially our basic database schema and is subject to change.
    I have also set explicit primary keys for ease of use although it should be noted that Django can handle this on
    its own by default. I also want to note that the many to Many relationships may change but for now they are there
    for flexibility. I have added first positional arguments to almost all the database fields to designate 
    human-readable names which is a little overkill but I want it to be as easy to read as possible
    
    Remember the three-step guide to making model changes:

    -Change your models (in models.py). 
    -Run python manage.py makemigrations to create migrations for those changes
    -Run python manage.py migrate to apply those changes to the database.
"""

# Define a user profile model to extend user information with roles and additional details
class UserProfile(models.Model):
    class Role(models.TextChoices):  # Role iterator
        PLAYER = 'PL', _('Player')
        GAME_OWNER = 'GO', _('Game Owner')
        ADMIN = 'AD', _('Admin')

    user_id = models.AutoField(primary_key=True)  # Explicit primary key
    email = models.EmailField("email address", max_length=200, unique=True)  # Cannot use same email twice
    join_date = models.DateTimeField("date joined", auto_now_add=True)  # Auto-set to now when object is created
    role = models.CharField("user role", max_length=2, choices=Role.choices, default=Role.PLAYER)  # Set default role as Player

# Define a game model that includes basic information about a game
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)  # Explicit primary key
    title = models.CharField("game title", max_length=200)
    developer = models.ForeignKey(UserProfile, verbose_name="game developer", on_delete=models.CASCADE)  # Link a game to a developer
    release_date = models.DateField("release date")
    description = models.TextField("game description")

# Model to track player performance in games, including ELO rating and match outcomes
class PlayerPerformance(models.Model):
    performance_id = models.AutoField(primary_key=True)  # Explicit primary key
    player = models.ForeignKey(UserProfile, verbose_name="player", on_delete=models.CASCADE)  # Link performance to a specific player
    game = models.ForeignKey(Game, verbose_name="related game", on_delete=models.CASCADE)  # Link performance to a specific game
    elo_rating = models.IntegerField("ELO rating", default=1000)  # Starting ELO rating
    matches_played = models.IntegerField("matches played", default=0)
    matches_won = models.IntegerField("matches won", default=0)
    matches_lost = models.IntegerField("matches lost", default=0)

# Leaderboard model to track top player performances per game.
class Leaderboard(models.Model):
    leaderboard_id = models.AutoField(primary_key=True)  # Explicit primary key
    game = models.ForeignKey(Game, verbose_name="associated game", on_delete=models.CASCADE)  # Link a leaderboard to a specific game
    player_performance = models.ManyToManyField(PlayerPerformance, verbose_name="player performances")  # Many-to-many link for player performances

# Event model for organizing game tournaments and related activities.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)  # Explicit primary key
    name = models.CharField("event name", max_length=200)
    game = models.ForeignKey(Game, verbose_name="associated game", on_delete=models.CASCADE)  # Link an event to a specific game
    start_date = models.DateTimeField("start date")
    end_date = models.DateTimeField("end date")
    organizer = models.ForeignKey(UserProfile, verbose_name="event organizer", related_name='organized_events', on_delete=models.CASCADE)  # Link to organizer
    participants = models.ManyToManyField(PlayerPerformance, verbose_name="event participants")  # Many-to-many relationship for event participants
