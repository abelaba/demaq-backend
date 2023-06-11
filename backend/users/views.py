from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import NewUser
from .serializers import MyUserSerializer
from rest_framework import permissions

# views here.
class MyUserView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format='json'):
        users=NewUser.objects.all()
        serialized_users=MyUserSerializer(users,many=True)
        return Response(serialized_users.data)
    
    def post(self, request, format='json'):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def put(self,request,format='json'):
        username=request.data.get("username")
        email=request.data.get("username")
        if username is None:
            return Response({"username":"is required"},status=400)
        if email is None:
            return Response({"email":"is required"},status=400)
        try:
            user=NewUser.objects.filter(username=username)
            if request.data.get("role") is None:
                return Response({"message":"role is required"},status=400)
            user.update(role=request.data.get("role"))
            return Response({"message":" role updated"},status=200)
        except:
            return Response({"message":"Could not found user "},status=404)


from rest_framework import generics

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = MyUserSerializer
