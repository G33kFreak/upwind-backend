from rest_framework import serializers

from relapses.models import Relapse


class RelapseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relapse
        fields = [
            'datetime',
            'reason',
        ]
