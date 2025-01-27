# Generated by Django 4.2.14 on 2024-08-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flight",
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
                ("aircraft", models.CharField(blank=True, max_length=256, null=True)),
                ("origin", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "destination",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("departure_date", models.DateField(blank=True, null=True)),
                ("departure_time", models.TimeField(blank=True, null=True)),
                ("arrival_date", models.DateField(blank=True, null=True)),
                ("arrival_time", models.TimeField(blank=True, null=True)),
                (
                    "flight_time",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
            ],
        ),
    ]
