from django.contrib import admin
from .models import UserProfile, Game, Leaderboard, PlayerPerformance, Event

admin.site.register(UserProfile)
admin.site.register(Game)
admin.site.register(Leaderboard)
admin.site.register(PlayerPerformance)
admin.site.register(Event)
# Register your models here.
