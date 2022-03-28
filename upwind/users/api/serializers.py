from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'first_name', 'email', 'password']

    def create(self) -> User:
        return User.objects.create_user(
            email=self.validated_data.get('email'),
            password=self.validated_data.get('password'),
            first_name=self.validated_data.get('first_name'),
            is_active=False,
        )

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'email', 'first_name', 'is_active']