from django.urls import path

from . import views

app_name = "game"

urlpatterns = [
    # ex: /game/collection/
    path("collection/", views.Collection.as_view(), name="collection"),
    # ex: /game/loadout/
    path("loadout/", views.Loadout.as_view(), name="loadout"),
    # ex: /game/loadout/add/1edb8915-2b32-417e-ad1a-07e4bf0418d2/
    path("loadout/add/<uuid:uid>/", views.AddToLoadout.as_view(), name="add-to-loadout"),
    # ex: /game/loadout/remove/1edb8915-2b32-417e-ad1a-07e4bf0418d2/
    path(
        "loadout/remove/<uuid:uid>/",
        views.RemoveFromLoadout.as_view(),
        name="remove-from-loadout",
    ),
    # ex: /game/encounter/
    path("encounter/", views.Encounter.as_view(), name="encounter"),
    # ex: /game/decompile/1edb8915-2b32-417e-ad1a-07e4bf0418d2/
    path("decompile/<uuid:uid>", views.Decompile.as_view(), name="decompile"),
]
