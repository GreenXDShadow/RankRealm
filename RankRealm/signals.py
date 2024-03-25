from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# TODO: See if we can find a way to refine these signals into one but for now I cant be bothered.

# @receiver(post_save, sender=User)
def create_player(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    Profile.objects.create(user=user, role=Profile.Role.PLAYER)  # Explicitly create and link Profile
    return user


"""EXAMPLE USAGE: player = create_player('playerusername', 'player@example.com', 'playerpassword')"""


def create_game_owner(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    Profile.objects.create(user=user, role=Profile.Role.GAME_OWNER)  # <-- difference is that here we change the
    # role. if we can pass it in as an arg instead that condenses our 3 defs into 1
    return user


"""EXAMPLE USAGE: game_owner = create_game_owner('gameownerusername', 'gameowner@example.com', 'gameownerpassword')"""


def create_admin(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    Profile.objects.create(user=user, role=Profile.Role.ADMIN)  # Explicitly create and link Profile
    return user


"""EXAMPLE USAGE: admin = create_admin('adminusername', 'admin@example.com', 'adminpassword')"""
