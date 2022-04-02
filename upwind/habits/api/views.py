from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from habits.api.serializers import HabitSerializer, HabitsCreateSerializer, HabitsListSerializer
from habits.models import Habit

class HabitsListAPIView(ListCreateAPIView):
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HabitsCreateSerializer
        else:
            return HabitsListSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return super().create(request, *args, **kwargs)

class HabitAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    lookup_field = 'id'
    queryset = Habit.objects.all()
    


