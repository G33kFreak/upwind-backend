from rest_framework import serializers

from habits.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name', 'time_spend_monthly', 'money_spend_monthly', 'user']

    def create(self) -> Habit:
        return Habit.objects.create(
            name=self.validated_data.get('name'),
            time_spend_monthly=self.validated_data.get('time_spend_monthly'),
            money_spend_monthly=self.validated_data.get('money_spend_monthly'),
            user=self.validated_data.get('user')
        )

class HabitsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name', 'time_spend_monthly', 'money_spend_monthly']