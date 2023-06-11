from rest_framework import serializers
from usermanagement.models import UserStatus

class UserSerializer(serializers.Serializer):
    logged = serializers.CharField()
    class Meta:
        model=UserStatus