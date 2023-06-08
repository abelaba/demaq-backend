from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import NewUser
from .serializers import MyUserSerializer
# views here.
class MyUserView(APIView):

    def post(self, request, format='json'):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors)