from django.db import models
from datetime import datetime,date

def broadcast_audio_directories(instance,filename):
    return '{filename}'.format(filename=filename)

class BroadCastModel(models.Model):
    broadcaster=models.ForeignKey('users.NewUser',on_delete=models.CASCADE,null=True)
    broadcast_date = models.CharField(default=datetime.today().strftime("%Y-%m-%d"),max_length=300)
    broadcasted_audio_title=models.CharField(max_length=250,unique=True,primary_key=True)
    broadcasted_file=models.FileField(upload_to=broadcast_audio_directories)


    def __str__(self):
       return f"broadcaster {self.broadcaster} date {self.broadcast_date} broadcasted audio {self.broadcasted_audio_title} broadcasted_file {self.broadcasted_file}"
class StackModel(models.Model):
    title=models.CharField(max_length=500,primary_key=True)
    broadcast_audios =  models.ManyToManyField(BroadCastModel)

    def __str__(self) -> str:
        return self.title