import typing as t

from django.contrib import admin
from django.utils.html import format_html

from . import models


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    fields = (
        "user",
        "upgrade_parts",
        "loadout",
    )
    readonly_fields = ("user",)


@admin.register(models.BotSpecies)
class BotSpeciesAdmin(admin.ModelAdmin):
    list_display = ("name", "sprite_icon", "sprite", "mods_from")
    readonly_fields = ("sprite_thumbnail",)

    def sprite_thumbnail(self, obj: models.BotSpecies) -> str:
        return format_html(
            '<img width="128" style="image-rendering: pixelated" src="{}">',
            obj.sprite.url,
        )

    def sprite_icon(self, obj: models.BotSpecies) -> str:
        return format_html(
            '<img width="16" style="image-rendering: pixelated" src="{}">',
            obj.sprite.url,
        )


@admin.register(models.Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "species", "owner")
    fields = ("uid", "owner", "species", "name", "level")
    readonly_fields = ("uid",)
