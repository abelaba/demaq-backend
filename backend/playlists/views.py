from django.shortcuts import render
from .models import AudioModel,PlaylistModel
from .serializers import AudioModelSerializer,PlaylistSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class PlayListViews(APIView):
    def get(self,request,format=None):
        playlists_raw=PlaylistModel.objects.all()
        playlists_serialized=PlaylistSerializers(playlists_raw,many=True)
        playlists=playlists_serialized.data
        return Response(playlists)
class PlayListView(APIView):
    def post(self,request,format=None):
        title=request.data.get("title")
        if title is None:
            return Response({"title":"is required"},status=400)
       
        try:
            playlist_raw=PlaylistModel.objects.create(playlist_title=title)
            playlist_serialized=PlaylistSerializers(playlist_raw)
            playlist=playlist_serialized.data
            return Response(playlist)
        except:
            return Response({"status":"could not create database change the name"},status=500)
        # played_audio_name=request.data.get("played_audio_name")
        # if played_audio_name is None:
        #     return Response({"played_audio_name":"is required"},status=400)
        # audio_file=request.data.get("audio")
        # if audio_file is None:
        #     return Response({"audio":"is required"},status=400)
        # check_str=type(request.data.get("audio")) is str
        # if check_str is True:
        #         return Response({"audio":"should be file"},status=400)
        return Response("good")
           

        
    def get_queryset(self):
        return super().get_queryset()
    

