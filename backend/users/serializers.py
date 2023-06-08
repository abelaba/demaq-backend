from .models import NewUser
from rest_framework import serializers
class MyUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True,
            min_length=5,
            max_length=20
            ),
    password = serializers.CharField(
            required=True,
            max_length=256
            )
    role = serializers.CharField(
            required=True,
            max_length=256
            )
   

    class Meta:
        model = NewUser
        fields = ('username', 'password','role',)

    def create(self, validated_data):
        user = NewUser.objects.create_user(validated_data['username'], validated_data["password"],validated_data["role"])
        return user
