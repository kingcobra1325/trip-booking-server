from django.db import models


class Flight(models.Model):
    aircraft = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    origin = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    destination = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    departure_date = models.DateField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)

    arrival_date = models.DateField(null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)

    flight_time = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
