from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id',
            'name',
            'time_spend_monthly',
            'money_spend_monthly',
        ]


class HabitsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id',
            'name',
            'time_spend_monthly',
            'money_spend_monthly',
            'user'
        ]

class HabitsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id',
            'name',
            'time_spend_monthly',
            'money_spend_monthly',
        ]