from uuid import UUID
import random

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views import View
from django.views.generic import ListView, DetailView

from . import models


class Collection(LoginRequiredMixin, ListView):
    template_name = "bots/collection.html"

    def get_queryset(self):
        return models.Bot.objects.filter(owner=self.request.user.player)


class Loadout(LoginRequiredMixin, ListView):
    template_name = "bots/loadout.html"

    def get_queryset(self):
        return self.request.user.player.loadout.all()


class AddToLoadout(LoginRequiredMixin, View):
    template_name = "bots/add_to_loadout.html"

    def get(self, request: HttpRequest, *, uid: UUID) -> HttpResponse:
        bot = get_object_or_404(models.Bot, uid=uid, owner=request.user.player)

        # if this bot is already in the loadout, there's nothing to do.
        # we can just redirect to index here because the user can only get here
        # if they're messing around with URLs anyway.
        if bot.is_in_loadout:
            return redirect("index")

        # if the user has space in their loadout, we can fast-forward this request.
        try:
            request.user.player.add_bot_to_loadout(bot)
        except models.Player.NoLoadoutSlotsAvailable:
            pass  # better luck next time
        else:
            return redirect("game:loadout")  # success!

        loadout_bots = request.user.player.loadout.all()

        return render(
            request,
            self.template_name,
            {"bot": bot, "loadout": loadout_bots},
        )

    def post(self, request: HttpRequest, *, uid: UUID) -> HttpResponse:
        return render(request, self.template_name)


class RemoveFromLoadout(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, *, uid: UUID) -> HttpResponse:
        bot = get_object_or_404(models.Bot, uid=uid, owner=request.user.player)
        request.user.player.loadout.remove(bot)
        return redirect("game:loadout")


class Encounter(LoginRequiredMixin, View):
    template_name = "bots/encounter.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        ids = models.BotSpecies.objects.values_list("pk", flat=True)
        species = models.BotSpecies.objects.get(pk=random.choice(ids))
        bot = models.Bot.objects.create(
            name=species.name,
            level=random.randint(1, 101),
            species=species,
            owner=request.user.player,
        )
        return render(request, self.template_name, {"bot": bot})


class Decompile(LoginRequiredMixin, DetailView):
    template_name = "bots/decompile.html"
    model = models.Bot
    slug_field = "uid"
    slug_url_kwarg = "uid"

    def post(self, request: HttpRequest, *, uid: str) -> HttpResponse:
        bot = self.get_object()
        request.user.player.upgrade_parts += bot.parts_value
        bot.delete()
        request.user.player.save(update_fields=["upgrade_parts"])
        return redirect("game:collection")
