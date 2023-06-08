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
from file_processing import activity as activity_views
from broadcast.views import BroadcastView ,BroadcastViews
from broadcast.activity import BroadcastingToday,BroadcastingAllYear
from users.views import MyUserView,UserDetail
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
    path("api/activity/recordingtoday/",activity_views.RecordingToday.as_view()),
    path("api/activity/recordingthisyear/",activity_views.RecordingAllYear.as_view()),
    # Broadcaster
    
    path("api/broadcasts/",BroadcastViews.as_view()),
    path("api/broadcast/",BroadcastView.as_view()),
    # Broadcaster Activity
    
    path("api/activity/broadcasttoday/",BroadcastingToday.as_view()),
    path("api/activity/broadcastyear/",BroadcastingAllYear.as_view()),
    
    
    path("api/user/",MyUserView.as_view()),
    path("api/userdetail/<int:pk>",UserDetail.as_view())
]
