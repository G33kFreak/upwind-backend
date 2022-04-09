from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from relapses.api.serializers import RelapseSerializer, RelapseCreateSerializer
from relapses.models import Relapse
from relapses.services import RelapseReportCreator


class RelapseListAPIView(ListCreateAPIView):
    def get_queryset(self):
        habit = self.request.data.get('habit', None)
        if habit == None:
            return Relapse.objects.filter(user=self.request.user)
        else:
            return Relapse.objects.filter(user=self.request.user, habit=habit)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RelapseCreateSerializer
        else:
            return RelapseSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return super().create(request, *args, **kwargs)


class RelapseAPIView(RetrieveUpdateDestroyAPIView):
    serializer_calss = RelapseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Relapse.objects.filter(user=self.request.user)


class RelapseReportAPIView(APIView):
    def get(self, request):
        return Response(RelapseReportCreator('', None)())
