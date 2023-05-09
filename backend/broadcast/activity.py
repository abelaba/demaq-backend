"""
In this module we will track user activities
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BroadCastModel
from .broad_cast_processing import BroadcastingProcessors,BroadcastingProcessor
from rest_framework import permissions
from datetime import datetime

class BroadcastingToday(APIView,BroadcastingProcessors):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        broadcasting_today=0
        broadcasts=self.get_broadcasts(request=request)
        if broadcasts.status_code is not 200:
            return broadcasts
        
        dates_audio_created=[]
        for broadcast in broadcasts.data:
            data=broadcast["broadcast_date"]
            dates_audio_created.append(data)
        today=datetime.today().strftime('%d')
        
        for each_day in dates_audio_created:
            date_format=datetime.strptime(each_day,'%Y-%m-%d')
            day_created=str(date_format.day)
            if(len(day_created)==1):
                day_created="0"+day_created
            if(day_created==today):
                broadcasting_today+=1
        if broadcasting_today==0:
            return Response({"No broadcasting today"},status=404)
        return Response({"broadcasted today":broadcasting_today},status=200)
class BroadcastingAllYear(APIView,BroadcastingProcessors):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        broadcasts=self.get_broadcasts(request=request)
        if broadcasts.status_code is not 200:
            return broadcasts
        
        months_broadcasts_broadcasted=[]
        all_months={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        for audio in broadcasts.data:
            data=audio["broadcast_date"]
            months_broadcasts_broadcasted.append(data)
        this_year=datetime.today().strftime('%y')
        
        for each_day in months_broadcasts_broadcasted:
            date_format=datetime.strptime(each_day,'%Y-%m-%d')
            month_broadcasted=date_format.month
            all_months[month_broadcasted]+=1
        return Response({"broadcasts broadcasted this year":all_months},status=200)
    
    