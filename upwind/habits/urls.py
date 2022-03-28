from django.urls import path
from habits.api.views import HabitsListAPIView

urlpatterns = [
    path('habits/', HabitsListAPIView.as_view()),
]
