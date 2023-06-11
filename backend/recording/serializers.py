from rest_framework import serializers
from recording.models import RecoredModel

class RecordSerializer(serializers.Serializer):
    title=serializers.CharField(required=True)
    descr=serializers.CharField(required=True)
    audio_file=serializers.CharField(required=True)
    owner=serializers.CharField(required=True)
    created = serializers.CharField()
    recorded_day=serializers.IntegerField()
    class Meta:
        model=RecoredModel
        fields=['title','owner','descr','audio']