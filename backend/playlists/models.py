from django.db import models
from datetime import datetime,date

def play_audio_directories(instance,filename):
    return '{filename}'.format(filename=filename)

class AudioModel(models.Model):
    audio_title=models.CharField(max_length=250,unique=True,primary_key=True)
    audio_file=models.FileField(upload_to=play_audio_directories)


    def __str__(self):
       return f"{self.audio_title}"
class PlaylistModel(models.Model):
    playlist_title=models.CharField(max_length=500,primary_key=True)
    played_audios =  models.ManyToManyField(AudioModel)

    def __str__(self) -> str:
        return self.playlist_title
    