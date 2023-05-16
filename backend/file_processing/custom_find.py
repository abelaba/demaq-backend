""""
   Here we will find files and users
"""
from rest_framework.response import Response
from .models import AudioModel
from .serializers import AudioSerializer
class CustomFind():
    """
        Finds audio by updated_title name 
        404 if not found
        400 if title is not in request
        200 if found
    """
    
    def find_audio_by_updated_title(self,request,format=None,):
        if request.data.get("title") is None:
            return Response({"title":"is required"},status=400)
        try:
            audio=AudioModel.objects.get(title=request.data.get("updated_title"))
            serialized=AudioSerializer(audio)
            return Response(serialized.data,status=200)
        except:
            return Response({"message":"Could not found the audio by title name "},status=404)
    
    
    """
        Finds audio by title name 
        404 if not found
        400 if title is not in request
        200 if found
    """
    
    def find_audio_by_title(self,request,format=None,):
        if request.data.get("title") is None:
            return Response({"title":"is required"},status=400)
        try:
            audio=AudioModel.objects.get(title=request.data.get("title"))
            serialized=AudioSerializer(audio)
            return Response(serialized.data,status=200)
        except:
            return Response({"message":"Could not found the audio by title name "},status=404)
    """
        find  audio by name from file 
        return 
            404 if  audio file is not found
            200 if  audio is found
    """ 
    def find_audio_by_name(self,request,format=None):
        import os
        def find(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
        path=str(os.path.dirname(os.getcwd()))+"/mediafiles/"
        # return Response(os.path.dirname(os.getcwd()))
    
        audio_file=request.data.get("audio")
        name=str(audio_file)
        duplicate_audio=find(name=name,path=path)
        if duplicate_audio:
            return Response({"path":duplicate_audio},status=200)
        return Response({"message":"No audio file by this audio name check extension such as .mp3 or .mkv   "},status=404)
    """
        find  if title name is duplicate
        400 if  title name is duplicate
        200 if  succedd
    """
    def find_duplicate_by_title_name(self,request,format=None):
        try:
            duplicate_title=AudioModel.objects.get(title=request.data.get("title"))
            return Response({"message":"Title Already in use"},status=400)
        except:
            return Response({"success"},status=200)
    """
        find  if title name is duplicate
        400 if  title name is duplicate
        200 if  succedd
    """
    def find_duplicate_audio(self,request,format=None):
        duplicate_audio=self.duplicate_audio(request=request)
        if duplicate_audio:
            return "d"
            return Response({"message":"Audio File name already in use please rename the file`{file name should be unique}`"},status=409)
        else:
            return Response({"success"},status=200)
    

    """
    This will find name based on par rather than request method
    """
    def find_audio_by_name_2(self,name,format=None):
        import os
        def find(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
        path=str(os.path.dirname(os.getcwd()))+"/mediafiles/"
        # return Response(os.path.dirname(os.getcwd()))
    
        audio_file=name
        name=str(audio_file)
        duplicate_audio=find(name=name,path=path)
        if duplicate_audio:
            return Response({"path":duplicate_audio},status=200)
        return Response({"message":"No audio file by this audio name check extension such as .mp3 or .mkv   "},status=404)
        
    """
    This will delete audios from file
    """
    def find_audio_and_delete(self,name,format=None):
        import os
        def find(name,path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
        path=str(os.path.dirname(os.getcwd()))+"/mediafiles/"
        path_to_delete=find(name=name,path=path)
        if path_to_delete is not None:
            os.remove(path_to_delete)
            return Response({"message":"success"},status=200)
        else:
            return Response({"message":"could not found the data to delete"},status=404)
                
            