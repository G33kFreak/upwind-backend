from django.utils import timezone

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from habits.api.serializers import HabitSerializer, HabitsCreateSerializer
from habits.models import Habit

class HabitsListAPIView(ListCreateAPIView):
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HabitsCreateSerializer
        else:
            return HabitSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        request.data['start_date'] = timezone.now()
        return super().create(request, *args, **kwargs)

class HabitAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    