from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from usermanagement.models import UserStatus
from usermanagement.serializers import UserSerializer
from datetime import datetime

# Create your views here.

class UserStatusDetail(APIView):
    def get(self,request,format=None):
        userstatues=UserStatus.objects.all()
        userstatuesserialized=UserSerializer(userstatues,many=True)

        return Response(userstatuesserialized.data)
    def post(self,request,format=None):
        try:
            newstatus=UserStatus.objects.create()
        except:
            return Response("could not create status",status=500)

        return Response("created")

class TodaysLoggedUser(APIView):
    def get(self,request,format=None):
        all_logs_raw=UserStatus.objects.all()
        all_logs_serialized=UserSerializer(all_logs_raw,many=True)
        all_logs=all_logs_serialized.data
        today=datetime.today().strftime("%Y-%m-%d")
        todays_logged_user=0

        for logs in all_logs:
           if(logs['logged']==today):
               todays_logged_user+=1
            
        return Response({"today's logged user":todays_logged_user})
   
