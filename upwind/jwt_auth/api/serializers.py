from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import serializers
from users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    is_active = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        attrs['email'] = attrs.get('email').lower()
        validated_data = super().validate(attrs)
        request_user = User.objects.filter(email=attrs.get('email')).first()
        is_user_active: bool = request_user.is_active if request_user else False
        validated_data['refresh_token'] = validated_data.pop('refresh')
        validated_data['access_token'] = validated_data.pop('access')
        validated_data['is_active'] = is_user_active

        return validated_data

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    refresh_token = serializers.CharField()
    access_token = serializers.ReadOnlyField()
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = attrs.pop("refresh_token")
        validated_data = super().validate(attrs)
        print(validated_data)
        validated_data["access_token"] = validated_data.pop("access")
        validated_data["refresh_token"] = attrs["refresh"]
        return validated_data
