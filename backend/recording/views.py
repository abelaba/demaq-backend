"""
In this module we will track user activities
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RecoredModel
from rest_framework import permissions
from recording.recording_processing import SingleRecordProcessing,MultipleRecordProcessing
from datetime import datetime
from recording.serializers import RecordSerializer
import calendar


class Recording(APIView,SingleRecordProcessing,MultipleRecordProcessing):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        recordings=RecoredModel.objects.all();
        recording_serialized=RecordSerializer(recordings,many=True)
        return Response(recording_serialized.data)
    
    
    def post(self,request,format=None):
          validate_input_and_title=self.validate_input_and_title(request=request)
          if validate_input_and_title.status_code is not 200:
            return validate_input_and_title
          audio_file=request.data.get("audio")
          try:
            audio=RecoredModel.objects.create(audio_file=audio_file,owner=request.user,title=request.data.get('title'),descr=request.data.get('descr'))
            serializer=RecordSerializer   (audio)
            return Response(serializer.data)
          except:
              return Response({"error":"title already in user"},status=400)
    
    
class RecordingToday(APIView,SingleRecordProcessing,MultipleRecordProcessing):
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

class RecordingThisWeek(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        recordings = RecoredModel.objects.all()
        recording_serialized = RecordSerializer(recordings, many=True)
        all_days = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

        for recording in recording_serialized.data:
            recording_day = recording['recorded_day']
            day_name = calendar.day_name[recording_day]
            all_days[day_name] += 1

        return Response(all_days)