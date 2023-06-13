from rest_framework import serializers
from usermanagement.models import UserStatus,NewUsersLog,UserActivityTrack

class UserStatusSerializer(serializers.Serializer):
    logged = serializers.CharField()
    class Meta:
        model=UserStatus
class NewUserSerializer(serializers.Serializer):
    created_week=serializers.CharField()
    class Meta:
        model=NewUsersLog

class UserActivityTrackSerializer(serializers.Serializer):
    tracked = serializers.CharField()
    class Meta:
        model=UserActivityTrack