from django.db import transaction
from rest_framework import serializers

from users.models import User
from users.services import UserActivationCreator



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'first_name', 'email', 'password']

    @transaction.atomic
    def create(self, validated_data):
        return UserActivationCreator(validated_data=validated_data)()

    def validate(self, data):
        super().validate(data)
        self.create(data)
        return data

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'email', 'first_name', 'is_active']