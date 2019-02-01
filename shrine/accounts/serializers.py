from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField(min_length=8)


class LoginSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()
