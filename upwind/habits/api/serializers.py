from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
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
            'saved_time'
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
            'start_date'
        ]

# class HabitsListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Habit
#         fields = [
#             'id',
#             'name',
#             'time_spend_weekly',
#             'money_spend_weekly',
#             'days',
#             'start_date',
#             'saved_money',
#             'saved_time'
#         ]