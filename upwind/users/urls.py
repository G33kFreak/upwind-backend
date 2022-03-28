from django.urls import path
from users.api.views import RegisterAPIView, UserDataAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('me/', UserDataAPIView.as_view())
]
