# Generated by Django 5.0.4 on 2024-04-20 04:58

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=140)),
                ("description", models.TextField()),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("city", models.CharField(max_length=80)),
                ("price", models.IntegerField()),
                ("address", models.CharField(max_length=140)),
                ("beds", models.IntegerField()),
                ("bedrooms", models.IntegerField()),
                ("baths", models.IntegerField()),
                ("guests", models.IntegerField()),
                ("check_in", models.TimeField()),
                ("check_out", models.TimeField()),
                ("instant_book", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
