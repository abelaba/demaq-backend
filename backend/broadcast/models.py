from django.db import models
from datetime import datetime,date



class BroadCastModel(models.Model):

    broadcast_date = models.CharField(default=datetime.today().strftime("%Y-%m-%d"),max_length=300)
    broadcasted_audio_title=models.CharField(max_length=250,unique=True)
    broadcaster=models.ForeignKey('users.NewUser',on_delete=models.CASCADE)


    def __str__(self):
       return f"broadcaster {self.broadcaster} date {self.broadcast_date} broadcasted audio {self.broadcasted_audio_title}"
