from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Agreements, CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    terms_agreement = serializers.BooleanField(write_only=True)
    privacy_agreement = serializers.BooleanField(write_only=True)
    marketing_agreement = serializers.BooleanField(
        write_only=True, required=False, default=False
    )

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password",
            "name",
            "phone",
            "terms_agreement",
            "privacy_agreement",
            "marketing_agreement",
        )

    def validate(self, data: dict) -> dict:
        if not data.get("terms_agreement") or not data.get("privacy_agreement"):
            raise serializers.ValidationError("필수 약관에 동의해야 합니다.")
        return data


class EmailCheckSerializer(serializers.Serializer):
    email = serializers.EmailField()


class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(
        required=True, help_text="로그인에 사용할 이메일 (예: user@example.com)"
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type": "password"},
        help_text="로그인 비밀번호",
    )

    def validate(self, attrs: dict[str, str]) -> dict[str, str]:
        data = super().validate(attrs)
        return {
            "message": "로그인이 완료되었습니다.",
            "access_token": data["access"],
            "refresh_token": data["refresh"],
        }


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)

class GoogleLoginSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)

class GoogleCallbackSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)