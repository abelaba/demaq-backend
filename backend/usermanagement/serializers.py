from rest_framework import serializers
from usermanagement.models import UserStatus,NewUsersLog

class UserStatusSerializer(serializers.Serializer):
    logged = serializers.CharField()
    class Meta:
        model=UserStatus
class NewUserSerializer(serializers.Serializer):
    created_week=serializers.CharField()
    class Meta:
        model=NewUsersLog
