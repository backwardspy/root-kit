# Generated by Django 3.1.5 on 2021-01-20 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0002_botspecies_parts_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="upgrade_parts",
            field=models.IntegerField(default=0),
        ),
    ]
