from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:game_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:game_id>/leaderboard/", views.leaderboard, name="leaderboard"),
    # ex: /polls/5/vote/
    path("<int:game_id>/joingame/", views.join_game, name="joingame"),
]