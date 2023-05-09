"""
In this module we will track user activities
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AudioModel
from rest_framework import permissions
from file_processing.views import AudioView
from file_processing.fileprocessing import SingleAudioProcessing,MultipleAudioProcessing
from datetime import datetime

class RecordingToday(APIView,SingleAudioProcessing,MultipleAudioProcessing):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        recording_today=0
        audios=self.get_all_audio(request=request)
        if audios.status_code is not 200:
            return audios
        
        dates_audio_created=[]
        for audio in audios.data:
            data=audio["created"]
            dates_audio_created.append(data)
        today=datetime.today().strftime('%d')
        
        for each_day in dates_audio_created:
            date_format=datetime.strptime(each_day,'%Y-%m-%d')
            day_created=str(date_format.day)
            if(len(day_created)==1):
                day_created="0"+day_created
            if(day_created==today):
                recording_today+=1
        if recording_today==0:
            return Response({"No recording created today"},status=404)
        return Response({"recording creating today":recording_today},status=200)
class RecordingAllYear(APIView,SingleAudioProcessing,MultipleAudioProcessing):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        audios=self.get_all_audio(request=request)
        if audios.status_code is not 200:
            return audios
        
        months_audio_created=[]
        all_months={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        for audio in audios.data:
            data=audio["created"]
            months_audio_created.append(data)
        this_year=datetime.today().strftime('%y')
        
        for each_day in months_audio_created:
            date_format=datetime.strptime(each_day,'%Y-%m-%d')
            month_created=date_format.month
            all_months[month_created]+=1
        return Response({"recording creating this year":all_months},status=200)
    
    