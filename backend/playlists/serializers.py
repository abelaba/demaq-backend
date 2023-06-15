from rest_framework import serializers
from .models import AudioModel,PlaylistModel
class AudioModelSerializer(serializers.Serializer):
    audio_title= serializers.CharField(required=True)
    audio_file=serializers.CharField(required=True)
    class Meta:
        model=AudioModel
        fields = '__all__'

class PlaylistSerializers(serializers.Serializer):
    played_audios= AudioModelSerializer(many=True,required=True)
    playlist_title=serializers.CharField()
    class Meta:
        model=PlaylistModel
        fields='__all__'