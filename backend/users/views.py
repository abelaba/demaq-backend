from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import NewUser
from .serializers import MyUserSerializer
from rest_framework import permissions
from usermanagement.models import NewUsersLog

# views here.
class MyUserView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format='json'):

        users=NewUser.objects.all()
        serialized_users=MyUserSerializer(users,many=True)
        response= Response(serialized_users.data)
        response['Access-Control-Allow-Origin'] = "*"
        return response
    def post(self, request, format='json'):

        # Confirm password
        password=request.data.get("password")
        confirm_password=request.data.get("confirm_password")
        if password is None:
            return Response({"password":"is required"},status=400)
        if confirm_password is None:
            return Response({"confirm_password":"is requried"},status=400)
        if(password!=confirm_password):
            return Response({"password":"does not match"},status=400)
        serializer = MyUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            try:
                log_new_user=NewUsersLog.objects.create()
            except:
                return Response({"log":"could not be created"},status=500)
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
