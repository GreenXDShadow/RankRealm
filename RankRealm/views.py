from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def detail(request, game_id):
    return HttpResponse("You're looking at %s." % game_id)


def leaderboard(request, game_id):
    response = "You're looking at the leaderboard of %s."
    return HttpResponse(response % game_id)


def join_game(request, game_id):
    return HttpResponse("You're adding yourself to %s." % game_id)
