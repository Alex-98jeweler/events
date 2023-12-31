# Generated by Django 4.2.5 on 2023-09-27 00:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_event_creator_eventfollower_follower'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventfollower',
            unique_together={('event', 'follower')},
        ),
    ]
