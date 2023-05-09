from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import BroadCastModel
from .serializers import BroadCastSerializer
from .broad_cast_processing import BroadcastingProcessor,BroadcastingProcessors

# Create your views here.
class BroadcastViews(APIView,BroadcastingProcessors):
    def get(self,request,format=None):
        broadcastes=self.get_broadcasts(request=request)
        return broadcastes
class BroadcastView(APIView,BroadcastingProcessor):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request,format=None):
        broad_cast=self.create_broadcast(request=request)
        return broad_cast
        