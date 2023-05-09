from rest_framework import serializers
from .models import BroadCastModel
class BroadCastSerializer(serializers.Serializer):
    broadcast_date = serializers.CharField()
    broadcasted_audio_title= serializers.CharField(required=True)
    broadcaster=serializers.CharField(required=True)
    class Meta:
        model=BroadCastModel
        fields=['broadcaster','broadcasted_audio_title']