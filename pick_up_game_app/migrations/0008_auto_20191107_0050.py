# Generated by Django 2.2.7 on 2019-11-07 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pick_up_game_app', '0007_auto_20191106_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='player',
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Event_Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='pick_up_game_app.Event')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='pick_up_game_app.Player')),
            ],
        ),
    ]