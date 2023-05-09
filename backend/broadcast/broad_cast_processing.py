from rest_framework.response import Response
from .models import BroadCastModel
from .serializers import BroadCastSerializer
class BroadcastingProcessor:
    def create_broadcast(self,request,format=None):
        if request.data.get("title") is None:
            return Response({"title":"is required"},status=400)
        # return Response("j")
        broadcasted=BroadCastModel.objects.create(broadcasted_audio_title=request.data.get("title"),broadcaster=request.user)
        serialized=BroadCastSerializer(broadcasted)
        return Response(serialized.data)
class BroadcastingProcessors:
    def get_broadcasts(self,request,format=None):
        broadcasted=BroadCastModel.objects.all()
        broadcasted_serialized=BroadCastSerializer(broadcasted,many=True)
        return Response(broadcasted_serialized.data)