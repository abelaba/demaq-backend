from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AudioModel
from rest_framework import permissions,generics
from .serializers import AudioSerializer
from django.http import FileResponse


    
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

class AudioView(APIView):
    permission_classes=[permissions.IsAuthenticated]        
    def find_audio_by_title(self,request,format=None,):
        if request.data.get("title") is None:
            return Response({"title":"is required"},status=400)
        try:
            audio=AudioModel.objects.get(title=request.data.get("title"))
            serialized=AudioSerializer(audio)
            return Response(serialized.data,status=200)
        except:
            return Response({"message":"Could not found the audio "},status=404)
        
    # validating the input response
    def validate_input(self,request,format=None):
        check_str=type(request.data.get("audio")) is str
        if request.data.get("audio",False) is False:
            return Response({"audio":" is required"},status=400)
        elif check_str is True:
            return Response({"audio":"should be file"},status=400)
        elif request.data.get("title",False) is False:
            return Response({"message":" Title is required"},status=400)
        elif request.data.get("descr",False) is False:
            return Response({"descr":" is required"},status=400)
        else:
            return Response({"success"},status=200)
     # validating the input response
    def validate_input_except_descr(self,request,format=None):
        check_str=type(request.data.get("audio")) is str
        if request.data.get("audio",False) is False:
            return Response({"audio":" is required"},status=400)
        elif check_str is True:
            return Response({"audio":"should be file"},status=400)
        elif request.data.get("title",False) is False:
            return Response({"title":" is required"},status=400)
       
        else:
            return Response({"success"},status=200)
    def validate_duplicate_title(self,request,format=None):
        try:
            duplicate_title=AudioModel.objects.get(title=request.data.get("title"))
            return Response({"message":"Title Already in use"},status=400)
        except:
            return Response({"success"},status=200)
    def duplicate_audio(self,request,format=None):
        import os
        def find(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
        path=str(os.path.dirname(os.getcwd()))+"/mediafiles/"
        audio_file=request.data.get("audio")
        name=str(audio_file)
        duplicate_audio=find(name=name,path=path)
        if duplicate_audio:
            return Response({"path":duplicate_audio},status=200)
        return Response({"message":"No audio file by this name"},status=404)
        
        
    def validate_duplicate_audo(self,request,format=None):
        duplicate_audio=self.duplicate_audio(request=request)
        if duplicate_audio:
            return Response({"message":"Audio File name already in use please rename the file`{file name should be unique}`"},status=409)
        else:
            return Response({"success"},status=200)
    def validate_audio_input(self,request,format=None):
        check_str=type(request.data.get("audio")) is str
        if request.data.get("audio",False) is False:
            return Response({"audio":" is required"},status=400)
        elif check_str is True:
            return Response({"audio":"should be file"},status=400)
        return Response({"message":"Success"},status=200)
    def validate_audio_input_2(self,request,format=None):
        if request.data.get("audio",False) is False:
            return Response({"audio":" is required"},status=400)
        return Response({"message":"Success"},status=200)
        

    def delete_audio(self,request,format=None):
        duplicate_audio=self.duplicate_audio(request=request)
        try:
            import os   
            os.remove(duplicate_audio)
            return Response({"status":"deleted"},status=200)
        except:
            return Response({"status":"File Not found error"},status=404)
       
            
    def validate_all(self,request,format=None):
        validate=self.validate_input(request=request)
        if validate.status_code is 400:
            return validate
        validate_title=self.validate_duplicate_title(request=request)
        
        if validate_title.status_code is 400:
            return validate_title
        validate_audio=self.validate_duplicate_audo(request=request)
        
        if validate_audio.status_code is 409:
            return validate_audio
        else:
            return Response("success",status=200)
        
            
             
    def validate_all_except_title(self,request,format=None):
        validate=self.validate_input(request=request)
        if validate.status_code is 400:
            return validate
        if request.data.get("updated_title") is None:
                return Response({"update_title":"updated_title is requried"},status=400)
            
        validate_audio=self.validate_duplicate_audo(request=request)
        
        if validate_audio.status_code is 409:
            return validate_audio
        find_by_title=self.find_audio_by_title(request=request)
        if find_by_title is not 200:
            return find_by_title
        else:
            return Response("success",status=200)
    
        
        
    # get audio by title name
    def get(self,request,format=None):
        audio=self.find_audio_by_title(request=request)
        audio_validate_input=self.validate_audio_input_2(request=request)
        duplicate=self.duplicate_audio(request=request)
        if audio.status_code is not 200:
            return audio
        if audio_validate_input.status_code is not 200:
            return audio_validate_input
        if duplicate.status_code is 404:
            return duplicate
      
        return duplicate
    #  post or create an audio at /mediafiles/audio
    def post(self,request,format=None):
        validate_all=self.validate_all(request=request)
        
        if validate_all.status_code is not 200:
            return validate_all
        
        audio_file=request.data.get("audio")
        audio=AudioModel.objects.create(audio_file=audio_file,owner=request.user,title=request.data.get('title'),descr=request.data.get('descr'))
        serializer=AudioSerializer(audio)
        return Response(serializer.data)
    
    def put(self,request,format=None):
        validate_all_except_title=self.validate_all_except_title(request=request)
        if validate_all_except_title.status_code is not 200:
            return validate_all_except_title
        audio_file=request.data.get("audio")
        audio=AudioModel.objects.filter(title=request.data.get("title")).update(title=request.data.get("updated_title"),audio_file=audio_file,descr=request.data.get('descr'))
        return Response("updated",status=201)
    def delete(self,request,format=None):
        # delete_audio=self.delete_audio(request=request)
        # if delete_audio is not 200:
        #     return delete_audio
        validate_all_except_descr=self.validate_input_except_descr(request=request)
        if validate_all_except_descr.status_code is not 200:
            return validate_all_except_descr
        validate_duplicate_title= self.validate_duplicate_title(request=request)
        if validate_duplicate_title.status_code is 200:
            return Response({"message":"no audio by this title "},status=404)
        try:
            audio=AudioModel.objects.get(title=request.data.get("title")).delete()
        except:
            return Response({"message":"could not delete the the file"},status=500)
        return Response({"deleted"},status=200)
