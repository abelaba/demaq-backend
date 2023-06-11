from rest_framework import serializers
from rest_framework.response import Response
from scripts.models import Script
class ScriptSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
    content = serializers.CharField()    
    def create(self,validated_data):
        return Script.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)