# Generated by Django 3.1.5 on 2021-01-23 15:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_player_loadout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('efficacy', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('power', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.AlterField(
            model_name='bot',
            name='level',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='botspecies',
            name='parts_value',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='upgrade_parts',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.CreateModel(
            name='MovesetEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learn_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('bot_species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.botspecies')),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.technique')),
            ],
        ),
        migrations.AddField(
            model_name='botspecies',
            name='moveset',
            field=models.ManyToManyField(through='game.MovesetEntry', to='game.Technique'),
        ),
    ]