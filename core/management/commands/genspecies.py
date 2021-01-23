import json
import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a BotSpecies fixture file from PNGs in assets/"

    def handle(self, *args, **options):
        assets_path: Path = settings.BASE_DIR / "assets"
        media_path: Path = settings.MEDIA_ROOT
        fixture_path: Path = settings.BASE_DIR / "fixtures" / "bots.botspecies.json"
        species_path = Path("species")

        print(
            f"Loading assets from {assets_path} into {media_path} for fixture {fixture_path}"
        )

        media_path.mkdir(parents=True, exist_ok=True)
        fixture_path.parent.mkdir(parents=True, exist_ok=True)

        fixture_data = []

        for idx, sprite_path in enumerate(assets_path.glob("*.png"), start=1):
            fixture_data.append(
                {
                    "model": "bots.botspecies",
                    "pk": idx,
                    "fields": {
                        "name": sprite_path.stem,
                        "sprite": (species_path / sprite_path.name).as_posix(),
                        "mods_from": None,
                    },
                }
            )

            shutil.copy(sprite_path, media_path / species_path / sprite_path.name)

        with fixture_path.open("w") as f:
            json.dump(fixture_data, f)
