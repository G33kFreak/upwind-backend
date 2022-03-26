from django.urls import path
from users.api.views import RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
]
