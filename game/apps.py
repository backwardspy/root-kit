from django.apps import AppConfig
from django.db.models.signals import post_save
from django.conf import settings


class GameConfig(AppConfig):
    name = "game"

    def ready(self) -> None:
        from . import signals

        post_save.connect(
            signals.create_player_profile, sender=settings.AUTH_USER_MODEL
        )
