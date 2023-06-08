from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
def upload_audio_directory_to(instance,filename):
    return '{filename}'.format(filename=filename)
class AudioModel(models.Model):
    owner=models.ForeignKey('users.NewUser',on_delete=models.CASCADE)
    title=models.CharField(max_length=250,unique=True)
    descr=models.CharField(max_length=250)
    audio_file=models.FileField(upload_to=upload_audio_directory_to)
    created = models.CharField(default=datetime.today().strftime("%Y-%m-%d"),max_length=300)
    def __str__(self):
       return f"title {self.title}"

    