from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import NewUser
from .serializers import MyUserSerializer
from rest_framework import permissions
from usermanagement.models import NewUsersLog
from rest_framework import generics


# views here.
class MyUserView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format='json'):

        users=NewUser.objects.all()
        serialized_users=MyUserSerializer(users,many=True)
        response= Response(serialized_users.data)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    def post(self, request, format='json'):

        # Confirm password
        password=request.data.get("password")
        confirm_password=request.data.get("confirm_password")
        if password is None:
            response= Response({"password":"is required"},status=400)
            
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        if confirm_password is None:
            response=Response({"confirm_password":"is requried"},status=400)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        if(password!=confirm_password):
            response= Response({"password":"does not match"},status=400)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        serializer = MyUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            try:
                log_new_user=NewUsersLog.objects.create()
            except:
               response= Response({"log":"could not be created"},status=500)
               response["Access-Control-Allow-Origin"] = "*"
               response["Access-Control-Allow-Headers"] = "*"
               return response
            response= Response(serializer.data,status=200)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Headers"] = "*"
            return response
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


class UserByName(APIView):
    def get(self,request,format=None):
        username=request.data.get("username")
        if username is None:
            return Response({"username":"is required"},status=500)
        try:
            user_raw=NewUser.objects.get(username=username)
            user_serializer=MyUserSerializer(user_raw)
            return Response(user_serializer.data)
        except:
            return Response({"statuss","Not found"},status=400)
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = MyUserSerializer
class MyUserViews(generics.ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = MyUserSerializer