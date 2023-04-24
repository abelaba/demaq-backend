from rest_framework import serializers
from .models import AudioModel
class AudioSerializer(serializers.Serializer):
    class Meta:
        model=AudioModel
        fields=['title','owner','descr','audio_file']