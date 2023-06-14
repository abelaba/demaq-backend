from rest_framework import serializers
from .models import BroadCastModel,StackModel
class BroadCastSerializer(serializers.Serializer):
    broadcast_date = serializers.CharField()
    broadcasted_audio_title= serializers.CharField(required=True)
    broadcaster=serializers.CharField(required=True)
    broadcasted_file=serializers.CharField(required=True)
    class Meta:
        model=BroadCastModel
        fields = '__all__'

class StackSerializers(serializers.Serializer):
    broadcast_audios= BroadCastSerializer(many=True,required=True)
    title=serializers.CharField()
    class Meta:
        model=StackModel
        fields='__all__'