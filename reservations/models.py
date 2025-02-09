from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Restaurant(models.Model):
    seat_price = models.PositiveIntegerField()


class Table(models.Model):
    table_id = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.table_id}"


class Reservation(models.Model):
    table = models.OneToOneField(
        Table, on_delete=models.CASCADE, related_name="booking"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    cost = models.PositiveIntegerField()
    number_of_seats = models.PositiveSmallIntegerField()
