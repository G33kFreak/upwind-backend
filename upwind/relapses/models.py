from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from habits.models import Habit
from users.models import User


class Relapse(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255)
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name='relapses'
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class RelapseReport(models.Model):
    reason_to_avoid = models.CharField(max_length=255)
    reason_percentage = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0),
        ],
    )
    date_range_start = models.DateTimeField()
    date_range_end = models.DateTimeField()


