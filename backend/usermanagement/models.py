from django.db import models
from datetime import datetime


# Create your models here.
class UserStatus(models.Model):
    logged = models.CharField(default=datetime.today().strftime("%Y-%m-%d"),max_length=300)
