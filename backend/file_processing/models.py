from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def upload_audio_directory_to(instance,filename):
    return 'audio/{filename}'.format(filename=filename)
class AudioModel(models.Model):
    owner=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=250,unique=True)
    descr=models.CharField(max_length=250)
    audio_file=models.FileField(upload_to=upload_audio_directory_to)
    def __str__(self) -> str:
        return str(self.audio_file)
    