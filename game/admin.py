from django.contrib import admin
from django.utils.html import format_html

from . import models


class MovesetEntryInline(admin.TabularInline):
    model = models.MovesetEntry
    fields = (
        "technique",
        "learn_level",
    )
    ordering = ("learn_level",)
    extra = 1


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
    inlines = (MovesetEntryInline,)

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


@admin.register(models.Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ("name", "efficacy", "power")
