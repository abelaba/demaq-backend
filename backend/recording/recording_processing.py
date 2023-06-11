from rest_framework import generics
from rest_framework.response import Response
from .models import RecoredModel
from .serializers import RecordSerializer
from file_processing.custom_validators import CustomValidator
from file_processing.custom_find import CustomFind

    
class MultipleRecordProcessing(CustomValidator,CustomFind):
   
    """
    Get all the audios
    """
    def get_all_audio(self,request,format=None):
        audios=RecoredModel.objects.all()
        audio_serializer=RecordSerializer(audios,many=True)
        return Response(audio_serializer.data)
    
        
    """
    Gets audio by title and audio name
    
    send data as {
        "title":"title will be here"
        "audio":"audio name will be here"
    }
    returns the path of the audio
    """
    def get_audio_path(self,request,format=None):
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
        Create an audio file in media file directory
        {
            "audio":"add a file here"  the audio name should be different also the audio should not be string type
            "title":"Title of the audio here"
            "descr":"description about the audio"
            
        }
    """
    def post_audio(self,request,format=None):
        validate_input_and_title=self.validate_input_and_title(request=request)
        
        if validate_input_and_title.status_code is not 200:
            return validate_input_and_title
        audio_file=request.data.get("audio")
        audio=RecoredModel.objects.create(audio_file=audio_file,owner=request.user,title=request.data.get('title'),descr=request.data.get('descr'))
        serializer=RecordSerializer(audio)
        return Response(serializer.data)
    
    
    
    
    
    """
        update an audio file 
        {
            "audio":"add a file here"  the audio name should be differenet also the audio should not be string type
            "title":"Title of the audio here"
            "descr":"description about the audio"
            
        }
    """
    def put_audio(self,request,format=None):
        validate_input_and_updatedtitle=self.validate_input_and_updatedtitle(request=request)
        if validate_input_and_updatedtitle.status_code is not 200:
            return validate_input_and_updatedtitle
        
        audio_file=request.data.get("audio")
        audio=RecoredModel.objects.filter(title=request.data.get("title")).update(title=request.data.get("updated_title"),audio_file=audio_file,descr=request.data.get('descr'))        
        return Response({"message":"updated"},status=201)
    
    
    
    
    """"
    Delete the audio 
    """
    def delete_audio(self,request,format=None):
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
            audio=RecoredModel.objects.get(title=request.data.get("title")).delete()
        except:
            return Response({"message":"could not delete the file"},status=500)
        return Response({"deleted"},status=200)

    
class SingleRecordProcessing(CustomValidator,CustomFind):
   
    """
    Gets audio by title and audio name
    
    send data as {
        "title":"title will be here"
        "audio":"audio name will be here"
    }
    returns the path of the audio
    """
    def get_audio(self,request,format=None):
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
        return audio
    
        
    """
    Gets audio by title and audio name
    
    send data as {
        "title":"title will be here"
        "audio":"audio name will be here"
    }
    returns the path of the audio
    """
    def get_audio_path(self,request,format=None):
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
    def post_audio(self,request,format=None):
        validate_input_and_title=self.validate_input_and_title(request=request)
        
        if validate_input_and_title.status_code is not 200:
            return validate_input_and_title
        audio_file=request.data.get("audio")
        audio=RecoredModel.objects.create(audio_file=audio_file,owner=request.user,title=request.data.get('title'),descr=request.data.get('descr'))
        serializer=RecordSerializer(audio)
        return Response(serializer.data)
    
    
    
    
    
    """
        update an audio file 
        {
            "audio":"add a file here"  the audio name should be differenet also the audio should not be string type
            "title":"Title of the audio here"
            "descr":"description about the audio"
            
        }
    """
    def put_audio(self,request,format=None):
        validate_input_and_updatedtitle=self.validate_input_and_updatedtitle(request=request)
        if validate_input_and_updatedtitle.status_code is not 200:
            return validate_input_and_updatedtitle
        
        audio_file=request.data.get("audio")
        audio=RecoredModel.objects.filter(title=request.data.get("title")).update(title=request.data.get("updated_title"),audio_file=audio_file,descr=request.data.get('descr'))        
        return Response({"message":"updated"},status=201)
    
    
    
    
    """"
    Delete the audio 
    """
    def delete_audio(self,request,format=None):
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
            audio=RecoredModel.objects.get(title=request.data.get("title")).delete()
        except:
            return Response({"message":"could not delete the file"},status=500)
        return Response({"deleted"},status=200)
