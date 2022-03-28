from pyexpat import model
from django.db import models

from users.models import User

class Habit(models.Model):
    name = models.CharField(max_length=40)
    time_spend_monthly = models.FloatField(blank=True, default=None)
    money_spend_monthly = models.FloatField(blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)