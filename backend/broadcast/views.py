from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import BroadCastModel,StackModel
from .serializers import BroadCastSerializer,StackSerializers
from .broad_cast_processing import BroadcastingProcessor
from datetime import datetime,date
class BroadcastViews(APIView,BroadcastingProcessor):
    def get(self,request,format=None):
       broadcasts=self.get_broadcasts(request=request)
       return broadcasts
class BroadcastView(APIView,BroadcastingProcessor):
    permission_classes=[permissions.IsAuthenticated]
    def find_audio_by_name(self,audio_file,format=None):
        import os
        def find(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
        path=str(os.path.dirname(os.getcwd()))+"/mediafiles/"
        # return Response(os.path.dirname(os.getcwd()))
    
        name=str(audio_file)
        duplicate_audio=find(name=name,path=path)
        if duplicate_audio:
            return Response({"path":duplicate_audio},status=200)
        return Response({"message":"No audio file by this audio name check extension such as .mp3 or .mkv   "},status=404)
    
    def get(self,request,format=None):
        if(request.data.get("title") is None):
            return Response({"broadcaste title":"is required"},status=400)
        try:
            broadcasted=BroadCastModel.objects.get(broadcasted_audio_title=request.data.get("title"))
            broadcasted_serializer=BroadCastSerializer(broadcasted)
            find_broadcasted_file=self.find_audio_by_name(broadcasted_serializer.data['broadcasted_file'])
            return find_broadcasted_file
        except:
            return Response({"broadcasted file ":"is not found"},status=404)
    def post(self,request,format=None):
        if(request.data.get("title") is None):
            return Response({"title":"is required"},status=400)
        try:
            broadcasted=BroadCastModel.objects.get(broadcasted_audio_title=request.data.get("title"))
        
            return Response({"broadcast":"name in use"},status=400)
        except:
            check_str=type(request.data.get("audio")) is str

            if request.data.get("audio",False) is False:
                return Response({"audio":" is required"},status=400)
            elif check_str is True:
                return Response({"audio":"should be file"},status=400)
            broadcast=BroadCastModel.objects.create(broadcaster=request.user,broadcasted_audio_title=request.data.get("title"),broadcasted_file=request.data.get("audio"))
            broadcast_serialized=BroadCastSerializer(broadcast)
            return Response(broadcast_serialized.data)
        
class StackViews(APIView):
    def get(self,request,format=None):
        stackes=StackModel.objects.all()
        stacked_serializer=StackSerializers(stackes,many=True)
        return Response(stacked_serializer.data)

class StackView(APIView):
    def get(self,request,format=None):
        title_of_broadcast=request.data.get("title")
        if title_of_broadcast is None:
            return Response({"title":"is required"},status=400)
        try:
            stack=StackModel.objects.get(title=request.data.get("title"))
            stack_serialized=StackSerializers(stack)
            return Response(stack_serialized.data,status=201)
        except:
            return Response({"stack":"not found"},status=404)

    def post(self,request,format=None):
        title_of_stack=request.data.get("title")
        if title_of_stack is None:
            return Response({"title":"is required"},status=400)
        
        try:
            stack=StackModel.objects.get(title=title_of_stack)
            return Response({"name":"in use"})
        except:
            pass
        stack=StackModel.objects.create(title=title_of_stack)
        
        stack_serializer=StackSerializers(stack)
        return Response(stack_serializer.data)
    def put(self,request,format=None):
        title_of_stack=request.data.get("title")
        if title_of_stack is None:
            return Response({"title":"is required"},status=400)
        broadcast=request.data.get("broadcast")
        if broadcast is None:
            return Response({"broadcast":"is required"},status=400)
        try:
            broadcasted=BroadCastModel.objects.get(broadcasted_audio_title=broadcast)
            
        except:
            return Response({"broadcast":" audio not found or not ready to broadcast"},status=400)
        
        broadcasted_serialized=BroadCastSerializer(broadcasted)
        add_to_broadcast=broadcasted_serialized.data["broadcasted_audio_title"]
        # try:
        #     broadcast=BroadCastModel.objects.get(broadcast)
        # except:
        #     return Response({"broadcast":"is not in the system"},status=404)
        stack_raw=StackModel.objects.get(title=title_of_stack)
        stack_serializer=StackSerializers(stack_raw)
        stack=stack_serializer.data
        broadcasted_audios=stack["broadcast_audios"]
        to_broadcast=[]
        for broadcasted in broadcasted_audios:
            to_broadcast.append(broadcasted["broadcasted_audio_title"])
        to_broadcast.append(add_to_broadcast)
        
        stack_raw.broadcast_audios.set(
            to_broadcast
                )
        stack_serializer=StackSerializers(stack_raw)
        return Response(stack_serializer.data)
    def delete(self,request,format=None):
        title_of_broadcast=request.data.get("title")
        if title_of_broadcast is None:
            return Response({"title":"is required"},status=400)
        try:
            stack=StackModel.objects.get(title=request.data.get("title"))
            stack_serialized=StackSerializers(stack)

            stack.delete()
            return Response("deleted")
        except:
            return Response({"stack":"not found"},status=404)

class StackPaths(APIView):
    def find_audio_by_name(self,audio_file,format=None):
        import os
        def find(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
        path=str(os.path.dirname(os.getcwd()))+"/mediafiles/"
        # return Response(os.path.dirname(os.getcwd()))
    
        name=str(audio_file)
        duplicate_audio=find(name=name,path=path)
        if duplicate_audio:
            return Response({"path":duplicate_audio},status=200)
        return Response({"message":"No audio file by this audio name check extension such as .mp3 or .mkv   "},status=404)
    def get(self,request,format=None):
        title_of_broadcast=request.data.get("title")
        paths=[]
        if title_of_broadcast is None:
            return Response({"title":"is required"},status=400)
        try:
            stack=StackModel.objects.get(title=request.data.get("title"))
            stack_serialized=StackSerializers(stack)
            broadcast_audios=stack_serialized.data["broadcast_audios"]
            files=[]
            for broadcast in broadcast_audios:
                find_broadcasted_file=self.find_audio_by_name(broadcast['broadcasted_file'])
                files.append(find_broadcasted_file.data['path'])

                

            return Response(files,status=201)
        except:
            return Response({"stack":"not found"},status=404)

class StackOne(APIView):
    
    def delete(self,request,format=None):
        title_of_stack=request.data.get("title")
        if title_of_stack is None:
            return Response({"title":"is required"},status=400)
        broadcast=request.data.get("broadcast")
        if broadcast is None:
            return Response({"broadcast":"is required"},status=400)
        try:
            broadcasted=BroadCastModel.objects.get(broadcasted_audio_title=broadcast)
            
        except:
            return Response({"broadcast":" audio not found or not ready to broadcast"},status=400)
        
        broadcasted_serialized=BroadCastSerializer(broadcasted)
        add_to_broadcast=broadcasted_serialized.data["broadcasted_audio_title"]
        # try:
        #     broadcast=BroadCastModel.objects.get(broadcast)
        # except:
        #     return Response({"broadcast":"is not in the system"},status=404)
        stack_raw=StackModel.objects.get(title=title_of_stack)
        stack_serializer=StackSerializers(stack_raw)
        stack=stack_serializer.data
        broadcasted_audios=stack["broadcast_audios"]
        to_broadcast=[]
        for broadcasted in broadcasted_audios:
            print(broadcasted["broadcasted_audio_title"]==add_to_broadcast)
            if(broadcasted["broadcasted_audio_title"]!=add_to_broadcast):
             to_broadcast.append(broadcasted["broadcasted_audio_title"])
        
        stack_raw.broadcast_audios.set(
            to_broadcast
                )
        stack_serializer=StackSerializers(stack_raw)
        return Response(stack_serializer.data)
