from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from usermanagement.models import UserStatus,NewUsersLog
from usermanagement.serializers import UserStatusSerializer,NewUserSerializer
from datetime import datetime,date

# Create your views here.

class UserStatusDetail(APIView):
    def get(self,request,format=None):
        userstatues=UserStatus.objects.all()
        userstatuesserialized=UserStatusSerializer(userstatues,many=True)

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
        all_logs_serialized=UserStatusSerializer(all_logs_raw,many=True)
        all_logs=all_logs_serialized.data
        today=datetime.today().strftime("%Y-%m-%d")
        todays_logged_user=0

        for logs in all_logs:
           if(logs['logged']==today):
               todays_logged_user+=1
            
        return Response({"today's logged user":todays_logged_user})
   
class NewUsersView(APIView):
     def get(self,request,format=None):

        new_users_raw=NewUsersLog.objects.all()
        new_users_serialized=NewUserSerializer(new_users_raw,many=True)
        new_users=new_users_serialized.data
        my_date = date.today()                     
        year, week_num, day_of_week = my_date.isocalendar()
        this_week_created_users=0
        for new_user in new_users:
            if(new_user['created_week']==str(week_num)):
                this_week_created_users+=1


            
        return Response({"this week created users":this_week_created_users})
     def post(self,request,format=None):
         try:
             log_new_user=NewUsersLog.objects.create()
             return Response({"log":"created"},status=201)
         except:
             return Response({"log":"could not be created"},status=500)