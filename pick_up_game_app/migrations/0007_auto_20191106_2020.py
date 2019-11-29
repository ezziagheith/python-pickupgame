# Generated by Django 2.2.7 on 2019-11-06 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pick_up_game_app', '0006_event_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to=settings.AUTH_USER_MODEL),
        ),
    ]
