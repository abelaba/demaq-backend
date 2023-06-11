from django.db import models

# Create your models here.

class Script(models.Model):
    title=models.CharField(max_length=100,unique=True)
    content=models.TextField()