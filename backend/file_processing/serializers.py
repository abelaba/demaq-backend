from rest_framework import serializers
from .models import AudioModel
class AudioSerializer(serializers.Serializer):
    title=serializers.CharField(required=True)
    descr=serializers.CharField(required=True)
    audio_file=serializers.CharField(required=True)
    owner=serializers.CharField(required=True)
    class Meta:
        model=AudioModel
        fields=['title','owner','descr','audio_file']