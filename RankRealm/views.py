from django.shortcuts import render, redirect  # imported for redirect support

# Create your views here.
from django.contrib.auth import authenticate, login  # imported for login auth
from django.http import HttpResponse
from .models import *  # This imports all our models into here
from .signals import *


def index(request):
    return render(request, 'index.html')


def gameinfo(request, game_id):
    return HttpResponse("You're looking at %s." % game_id)


def userprofile(request, user_id):
    response = "You're looking at %s's profile."
    return HttpResponse(response % user_id)


def joingame(request, game_id):
    return HttpResponse("You're adding yourself to %s." % game_id)

# registration form
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # User authentication
        login(request, user)  # Log in the newly created user
        return redirect('index')  # Redirect to a success page or home page
    return render(request, 'login.html')  # Show the registration form again if not POST


# registration form
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = create_player(username, email, password)
        login(request, user)  # Log in the newly created user
        return redirect('index')
    return render(request, 'register.html')  # Show the registration form again if not POST