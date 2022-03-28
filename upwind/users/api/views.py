from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.api.serializers import RegisterSerializer, UserDataSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create()
        user.save()
        return Response(serializer.data)


class UserDataAPIView(RetrieveAPIView):
    serializer_class = UserDataSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
