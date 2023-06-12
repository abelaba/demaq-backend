from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import BroadCastModel
from .broad_cast_processing import BroadcastingProcessor
from datetime import datetime,date

class BroadcastView(APIView,BroadcastingProcessor):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        broadcastes=self.get_broadcasts(request=request)
        return broadcastes
    def post(self,request,format=None):
        broadcast=self.create_broadcast(request=request)
        return broadcast
