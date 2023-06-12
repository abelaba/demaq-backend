"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from users import views
from rest_framework import routers
from file_processing import views as file_processing_views

from broadcast.views import BroadcastView ,BroadcastViews
from broadcast.activity import BroadcastingToday,BroadcastingAllYear

from users.views import MyUserView,UserDetail

from scripts.views import ScriptsHome,ScriptsMany

from recording.views import RecordingThisWeek,RecordingToday,Recording


from usermanagement.views import UserStatusDetail,TodaysLoggedUser,NewUsersView

# Token views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# User views
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)



urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # Authentications
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # File Processing
    path('api/audio/', file_processing_views.AudioView.as_view()),
    path('api/audio/<int:pk>', file_processing_views.AudioViewGet.as_view()),
    path('api/audios/', file_processing_views.AudioViews.as_view()),
    # User Activities
    path("api/activity/recording/",Recording.as_view()),
    path("api/activity/recordingtoday/",RecordingToday.as_view()),
    path("api/activity/recordingthisweek/",RecordingThisWeek.as_view()),
    # Broadcaster
    
    path("api/broadcasts/",BroadcastViews.as_view()),
    path("api/broadcast/",BroadcastView.as_view()),
    # Broadcaster Activity
    
    path("api/activity/broadcasttoday/",BroadcastingToday.as_view()),
    path("api/activity/broadcastyear/",BroadcastingAllYear.as_view()),
    
    # Creating and getting users
    path("api/user/",MyUserView.as_view()),
    path("api/userdetail/<int:pk>",UserDetail.as_view()),

    #Scripts
    path("api/script/", ScriptsHome.as_view(), name="script"), 
    path("api/scripts/", ScriptsMany.as_view(), name="scripts"),

    # User status
    path("api/user/log/",UserStatusDetail.as_view(), name="userlog"),
    path("api/user/log/today/", TodaysLoggedUser.as_view(), name="todayloggeduser"),
    path("api/user/newusers/", NewUsersView.as_view(), name="newusers")

    
]
