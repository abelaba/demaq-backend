from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AudioModel
from rest_framework import permissions
from .serializers import AudioSerializer
# Create your views here.

class AudioView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        audios=AudioModel.objects.all()
        print(audios)
        return Response({"found":"all"})
    def post(self,request,format=None):
        check_str=type(request.data.get("audio")) is str
        if request.data.get("audio",False) is False:
            return Response({"message":"Audio File is required"},status=400)
        elif check_str is True:
            return Response({"message":"Audio File should not be string type"},status=400)
        audio_file=request.data.get("audio")
        # method uses for searching file name 
        # future uses for searching
        import os
        print(os.getcwd())
        def find(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
        path=str(os.path.dirname(os.getcwd()))+"/mediafiles/"
        name=str(audio_file)
        duplicate=find(name=name,path=path)
        if duplicate:
            return Response({"message":"Audio File name already in use please rename the file"},status=500)
        
        audio_created=AudioModel.objects.create(audio_file=audio_file,owner=request.user)
        return Response({"message":"Succesfully stored the audio file"})

