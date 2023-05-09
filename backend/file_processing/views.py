from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AudioModel
from rest_framework import permissions,generics
from .serializers import AudioSerializer
from .custom_validators import CustomValidator
from .custom_find import CustomFind

    
# Create your views here.
# get all audios
class AudioViews(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        audios=AudioModel.objects.all()
        serializer=AudioSerializer(audios,many=True)
        return Response(serializer.data)
# get a single audio by int:pk
class AudioViewGet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset=AudioModel.objects.all()
    serializer_class=AudioSerializer

class AudioView(APIView,CustomValidator,CustomFind):
    permission_classes=[permissions.IsAuthenticated]        
    
    def get_updated_audio(self,request,format=None):
        updated_audio=self.find_audio_by_name_2(name=request.data.get(("updated_title")))
        return updated_audio
    
        
    """
    Gets audio by title and audio name
    
    send data as {
        "title":"title will be here"
        "audio":"audio name will be here"
    }
    returns the path of the audio
    """
    def get(self,request,format=None):
        audio=self.find_audio_by_title(request=request)
        validate_audio_name_input=self.validate_audio_name_input(request=request)
        find_audio_by_name=self.find_audio_by_name(request=request)
        if audio.status_code is not 200:
            return audio
        if validate_audio_name_input.status_code is not 200:
            return validate_audio_name_input
        if find_audio_by_name.status_code is 404:
            return find_audio_by_name
        # find_audio_by_name=path of the audio
        return find_audio_by_name
    
        
    
    
    
    """
        Create an audio file in mediafile directory
        {
            "audio":"add a file here"  the audio name should be differenet also the audio should not be string type
            "title":"Title of the audio here"
            "descr":"description about the audio"
            
        }
    """
    def post(self,request,format=None):
        validate_input_and_title=self.validate_input_and_title(request=request)
        
        if validate_input_and_title.status_code is not 200:
            return validate_input_and_title
        audio_file=request.data.get("audio")
        audio=AudioModel.objects.create(audio_file=audio_file,owner=request.user,title=request.data.get('title'),descr=request.data.get('descr'))
        serializer=AudioSerializer(audio)
        return Response(serializer.data)
    
    
    
    
    
    """
        update an audio file 
        {
            "audio":"add a file here"  the audio name should be differenet also the audio should not be string type
            "title":"Title of the audio here"
            "descr":"description about the audio"
            
        }
    """
    def put(self,request,format=None):
        validate_input_and_updatedtitle=self.validate_input_and_updatedtitle(request=request)
        if validate_input_and_updatedtitle.status_code is not 200:
            return validate_input_and_updatedtitle
        
        audio_file=request.data.get("audio")
        audio=AudioModel.objects.filter(title=request.data.get("title")).update(title=request.data.get("updated_title"),audio_file=audio_file,descr=request.data.get('descr'))        
        return Response({"message":"updated"},status=201)
    
    
    
    
    """"
    Delete the audio 
    """
    def delete(self,request,format=None):
        # delete_audio=self.delete_audio(request=request)
        # if delete_audio is not 200:
        #     return delete_audio
        validate_all_except_descr=self.validate_input_except_descr(request=request)
        if validate_all_except_descr.status_code is not 200:
            return validate_all_except_descr
        find_audio_by_title=self.find_audio_by_title(request=request)
        if find_audio_by_title.status_code is not 200:
            return find_audio_by_title
        try:
            audio=AudioModel.objects.get(title=request.data.get("title")).delete()
        except:
            return Response({"message":"could not delete the file"},status=500)
        return Response({"deleted"},status=200)
