import typing as t
from uuid import uuid4

from django.db import models
from django.conf import settings


class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    loadout = models.ManyToManyField("Bot")

    upgrade_parts = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username

    class NoLoadoutSlotsAvailable(Exception):
        pass

    def has_space_in_loadout(self) -> int:
        return len(self.loadoutentry_set) < settings.BOT_MAX_LOADOUT_SIZE

    def add_bot_to_loadout(self, bot: "Bot") -> None:
        if not self.has_space_in_loadout:
            raise self.NoLoadoutSlotsAvailable
        self.loadout.add(bot)


class BotSpecies(models.Model):
    name = models.CharField(unique=True, max_length=settings.BOT_NAME_MAX_LENGTH)
    mods_from = models.OneToOneField(
        "BotSpecies",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="mods_to",
    )
    sprite = models.ImageField(upload_to="species")

    parts_value = models.IntegerField(default=10)

    class Meta:
        verbose_name_plural = "Bot species"

    def __str__(self) -> str:
        return self.name


class Bot(models.Model):
    uid = models.UUIDField(unique=True, db_index=True, default=uuid4)
    name = models.CharField(max_length=settings.BOT_NAME_MAX_LENGTH)
    level = models.IntegerField()
    species = models.ForeignKey(BotSpecies, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="bot_collection",
    )

    @property
    def parts_value(self) -> int:
        return self.species.parts_value

    @property
    def is_in_loadout(self) -> bool:
        return self.owner.loadout.filter(pk=self.pk).exists()

    def __str__(self) -> str:
        parts = [f"lvl{self.level}", self.name]
        if self.name != self.species.name:
            parts.append(f"({self.species.name})")
        return " ".join(parts)
