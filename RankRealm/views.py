from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def gameinfo(request, game_id):
    return HttpResponse("You're looking at %s." % game_id)


def userprofile(request, user_id):
    response = "You're looking at %s's profile."
    return HttpResponse(response % user_id)


def joingame(request, game_id):
    return HttpResponse("You're adding yourself to %s." % game_id)
