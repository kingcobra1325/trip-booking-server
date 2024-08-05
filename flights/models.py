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
    departure_dt = models.DateTimeField(null=True, blank=True)
    arrival_dt = models.DateTimeField(null=True, blank=True)
    flight_time = models.SmallIntegerField(null=True, blank=True)
