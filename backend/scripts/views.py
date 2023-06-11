from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from scripts.models import Script
from scripts.serializers import ScriptSerializer


# Create your views here.
class ScriptsMany(APIView):
    def get(self,request,format=None):
        scripts=Script.objects.all()
        scripts_serialized=ScriptSerializer(scripts,many=True)
        return Response(scripts_serialized.data)
    

class ScriptsHome(APIView):
    def get(self,request,format='json'):
        title = request.data.get("title")
        if title is None:
            return Response({"title":"is required"},status=400)
        try:
            script=Script.objects.get(title=title)
            serialized=ScriptSerializer(script)
            return Response(serialized.data,status=200)
        except:
            return Response({"message":"could not found script"},status=400)
           
       
    def post(self,request,format=None):
        try:
            serialized_script=ScriptSerializer(data=request.data)

            if serialized_script.is_valid():
                serialized_script.save()
                return Response(serialized_script.data,status=200)
        except:
            return Response({"title":"already in use"},status=400)
        return Response(serialized_script.errors,status=400)
    def put(self,request,format=None):
        title=request.data.get('title')
        content=request.data.get("content")
        if title is None:
            return Response({"title":"is required"})
        if content is None:
            return Response({"content":"is required"})
        sc=self.get(request=request)
        if sc.status_code is not 200:
            return sc

        try:
         script=Script.objects.filter(title=title)
         script.update(content=request.data.get('content'))
         return Response({"message":"updated"},status=201)
        except:
            return Response({"message":"could not found script"},status=404)
    def delete(self,request,format=None):
        title=request.data.get('title')
        
        if title is None:
            return Response({"title":"is required"})
        sc=self.get(request=request)
        if sc.status_code is not 200:
            return sc
        try:
         script=Script.objects.filter(title=title)
         script.delete()
         return Response({"message":"deleted"},status=201)
        except:
            return Response({"message":"could not found script"},status=404)

