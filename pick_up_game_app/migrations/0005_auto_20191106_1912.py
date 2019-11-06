# Generated by Django 2.2.7 on 2019-11-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pick_up_game_app', '0004_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game_type',
            field=models.CharField(choices=[('FC', 'Full Court: 5 vs 5'), ('HC', 'Half Court: 3 vs 3'), ('OO', 'Half Court: 1 vs 1'), ('SA', 'Shoot Around')], max_length=2),
        ),
    ]