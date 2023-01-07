from .models import UserNet
from rest_framework import serializers


class GetUserNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNet
        fields = "__all__"

class UserNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNet
        fields = ["username", "first_name", "last_name", "avatar", "bio", "gender", "email", "phone", "birthday"]

class UserNetPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNet
        fields = ["username", "first_name", "last_name", "avatar", "bio", "gender"]

