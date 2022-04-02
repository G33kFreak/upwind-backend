from django.db import models
from datetime import datetime, timezone
from users.models import User


class Habit(models.Model):
    name = models.CharField(max_length=40)
    time_spend_weekly = models.FloatField(blank=True, default=None)
    money_spend_weekly = models.FloatField(blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()

    @property
    def days(self) -> int:
        return (datetime.now(timezone.utc) - self.start_date).days

    @property
    def money_per_day(self) -> float:
        if self.money_spend_weekly != None:
            return round(self.money_spend_weekly / 7, 2)
        else:
            return 0

    @property
    def time_per_day(self) -> float:
        if self.time_spend_weekly != None:
            return round(self.time_spend_weekly / 7, 2)
        else:
            return 0

    @property
    def saved_money(self) -> float:
        return round(self.money_per_day * self.days, 2)

    @property
    def saved_time(self) -> float:
        return round(self.time_per_day * self.days, 2)
