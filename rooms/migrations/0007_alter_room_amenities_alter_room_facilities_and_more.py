# Generated by Django 5.0.4 on 2024-04-23 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_rename_house_rule_room_house_rules"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.amenity"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="facilities",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.facility"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="host",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rooms",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="house_rules",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.houserule"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="room_types",
                to="rooms.roomtype",
            ),
        ),
    ]
