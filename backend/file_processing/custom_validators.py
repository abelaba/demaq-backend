""""
    Custom Validator

"""



from rest_framework.response import Response
from .models import AudioModel
from .custom_find import CustomFind
class CustomValidator(CustomFind):
    
        
    """
        validates the input of the user
        404 if not found
        400 if  audio is not in request,audio is not file 
        400 if  title is not in request
        400 if  descr is not in request    
        200 if  succedd
    """
    def validate_input(self,request,format=None):
        check_str=type(request.data.get("audio")) is str
        if request.data.get("audio",False) is False:
            return Response({"audio":" is required"},status=400)
        elif check_str is True:
            return Response({"audio":"should be file"},status=400)
        elif request.data.get("title",False) is False:
            return Response({"title":" is required"},status=400)
        elif request.data.get("descr",False) is False:
            return Response({"descr":" is required"},status=400)
        else:
            return Response({"success"},status=200)
    """
        validates the input of the user except the descr
        404 if not found
        400 if  audio is not in request,audio is not file 
        400 if  title is not in request
        200 if  succedd
    """
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
        
  
    def validate_audio_input(self,request,format=None):
        check_str=type(request.data.get("audio")) is str
        if request.data.get("audio",False) is False:
            return Response({"audio":" is required"},status=400)
        elif check_str is True:
            return Response({"audio":"should be file"},status=400)
        return Response({"message":"Success"},status=200)
    
    """
    Validate if audio name is present
        format
        {
         "audio":"audio name here" 
        }
        audio type:str
    return 
        200 if request has audio name
        400 if request has no audio name
        
    """
    def validate_audio_name_input(self,request,format=None):
        if request.data.get("audio",False) is False:
            return Response({"audio":" is required should be str, name of the audio you want to ger"},status=400)
        return Response({"message":"Success"},status=200)
    
    
    
    """
         in top of validate_input it adds
         1 find if the title name is duplicate
    """
            
    def validate_input_and_title(self,request,format=None):
        validate=self.validate_input(request=request)
        if validate.status_code is 400:
            return validate
        find_dupliicate_by_title_name=self.find_duplicate_by_title_name(request=request)
        
        if find_dupliicate_by_title_name.status_code is not 200:
            return find_dupliicate_by_title_name
        
        find_audio_by_name=self.find_audio_by_name(request=request)        
        if find_audio_by_name.status_code is 200:
            return Response({"audio":" is already in mediafile"},status=400)
        return Response("validated",status=200)
        
    """
         in top of validate_input it adds
         1 searches the file to find the audio
                  If audio file is in system return 400
         2 requires you to add updatedtitle
        
    """ 
    def validate_input_and_updatedtitle(self,request,format=None):
        validate_input=self.validate_input(request=request)
        if validate_input.status_code is not 200:
            return validate_input
        if request.data.get("updated_title") is None:
                return Response({"update_title":"updated_title is requried"},status=400)
        find_audio_by_name=self.find_audio_by_name(request=request)
        if find_audio_by_name.status_code is 200:
            return Response({"audio":"audio is already in system"},status=400)
        find_audio_by_title=self.find_audio_by_title(request=request)
        if find_audio_by_title.status_code is not 200:
            return find_audio_by_title
        find_duplicate_audio_by_title=self.find_audio_by_updated_title(request=request)
        if find_duplicate_audio_by_title.status_code is 200:
            return Response({"updated_title":"is already in user find new name"},status=400)
        return Response("validated",status=200)
    
        
    
    
    
    
    
    
        

    def delete_audio(self,request,format=None):
        duplicate_audio=self.duplicate_audio(request=request)
        try:
            import os   
            os.remove(duplicate_audio)
            return Response({"status":"deleted"},status=200)
        except:
            return Response({"status":"File Not found error"},status=404)
    
  
     
  