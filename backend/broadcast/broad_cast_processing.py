from rest_framework.response import Response
from .models import BroadCastModel
from .serializers import BroadCastSerializer
class BroadcastingProcessor:
    def get_broadcasts(self,request,format=None):
        broadcasted=BroadCastModel.objects.all()
        broadcasted_serialized=BroadCastSerializer(broadcasted,many=True)
        return Response(broadcasted_serialized.data)
    def create_broadcast(self,request,format=None):
        if request.data.get("title") is None:
            return Response({"title":"is required"},status=400)
        broadcast_duplicated=self.get_broadcast(request=request)
        if broadcast_duplicated.status_code is  200:
            return Response({"title":"already in use"},status=400)
        try:
            broadcasted=BroadCastModel.objects.create(broadcasted_audio_title=request.data.get("title"),broadcaster=request.user)
            serialized=BroadCastSerializer(broadcasted)
            return Response(serialized.data)
        except:
            return Response({"erro"},status=500)
    def get_broadcast(self,request,format=None):
        if request.data.get("title") is None:
            return Response({"title":"is required"},status=400)
        try:
            broadcast=BroadCastModel.objects.get(broadcasted_audio_title=request.data.get("title"))
            return Response({"broadcast":"found"},status=200)
        except:
            return Response({"broadcast":"could not found broadcast"},status=404)


    