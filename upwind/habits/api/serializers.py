from venv import create
from rest_framework import serializers

from habits.models import Habit
from relapses.api.serializers import RelapseSerializer


class HabitSerializer(serializers.ModelSerializer):
    relapses = RelapseSerializer(many=True)

    class Meta:
        model = Habit
        fields = [
            'id',
            'name',
            'time_spend_weekly',
            'money_spend_weekly',
            'days',
            'start_date',
            'saved_money',
            'saved_time',
            'relapses'
        ]


class HabitsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id',
            'name',
            'time_spend_weekly',
            'money_spend_weekly',
            'user',
        ]


class HabitsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id',
            'name',
            'time_spend_weekly',
            'money_spend_weekly',
            'days',
            'start_date',
            'saved_money',
            'saved_time',
        ]
