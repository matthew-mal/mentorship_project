from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "phone", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    mentees = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username"
    )
    mentor = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "is_mentor",
            "phone",
            "email",
            "password",
            "mentees",
            "mentor",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
            validated_data.pop("password")
        return super().update(instance, validated_data)
