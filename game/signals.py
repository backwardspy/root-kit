from django.conf import settings
from . import models


def create_player_profile(
    sender, instance: settings.AUTH_USER_MODEL, created: bool, *args, **kwargs
) -> None:
    if created:
        models.Player.objects.create(user=instance)
    else:
        instance.player.save()
