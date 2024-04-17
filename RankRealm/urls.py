from django.urls import path

from . import views
from .views import * #imports data from views

urlpatterns = [
    # ex: /
    path("", views.index, name="index"),
    # ex: port/game/15
    path("game/<int:game_id>/", views.gameinfo, name="gameinfo"),
    # ex: port/user/10
    path("user/<int:user_id>/", views.userprofile, name="userprofile"),
    # ex: port/joingame/10/15
    path("joingame/<int:user_id>/<int:game_id>", views.joingame, name="joingame"),
    # port/register
    path('register/', views.register, name='register'),
    # port/login
    path('login/', views.login, name='login'),
]