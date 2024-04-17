from django.shortcuts import render, redirect  # imported for redirect support

# Create your views here.
from django.contrib.auth import authenticate, login  # imported for login auth
from django.http import HttpResponse
from .models import *  # This imports all our models into here
from .signals import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect



def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def gameinfo(request, game_id):
    return HttpResponse("You're looking at %s." % game_id)


def userprofile(request, user_id):
    response = "You're looking at %s's profile."
    return HttpResponse(response % user_id)


def joingame(request, game_id):
    return HttpResponse("You're adding yourself to %s." % game_id)

# registration form
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to a success page or home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# registration form
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return redirect('login')  # Redirect to a success page or home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form}) # Show the registration form again if not POST