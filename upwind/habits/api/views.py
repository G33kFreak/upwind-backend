from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from habits.api.serializers import HabitSerializer, HabitsListSerializer
from habits.models import Habit

class HabitsListAPIView(ListAPIView):
    serializer_class = HabitsListSerializer

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def post(self, request):
        data = request.data
        data['user'] = request.user
        serializer = HabitSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        habit = serializer.create()
        habit.save()
        return Response(serializer.data)
