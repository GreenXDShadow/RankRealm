from django.apps import AppConfig

class RankrealmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RankRealm'

    def ready(self):
        # Import signals inside ready method to avoid import problems
        from . import signals
