from rest_framework import status

from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.api.serializers import RegisterSerializer, UserDataSerializer


class RegisterAPIView(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    http_method_names = ["post"]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserDataAPIView(RetrieveAPIView):
    serializer_class = UserDataSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
