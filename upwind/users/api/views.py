from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from users.api.serializers import UserSerializer
from users.models import User

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create()
        user.save()
        return Response(serializer.data)
        