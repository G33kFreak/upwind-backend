from django.db import models

from habits.models import Habit


class Relapse(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255)
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name='relapses'
    )
