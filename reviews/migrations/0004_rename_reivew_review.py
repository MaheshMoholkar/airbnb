# Generated by Django 5.1a1 on 2024-06-12 17:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_alter_reivew_room_alter_reivew_user"),
        ("rooms", "0009_alter_photo_file"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Reivew",
            new_name="Review",
        ),
    ]
