# Generated by Django 5.0.4 on 2024-04-23 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0007_alter_room_amenities_alter_room_facilities_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="rooms.room",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rooms",
                to="rooms.roomtype",
            ),
        ),
    ]
