from django.db import models
from datetime import datetime,date
my_date = date.today()                      # Show actual date
year, week_num, day_of_week = my_date.isocalendar()

# Create your models here.
class UserStatus(models.Model):
    logged = models.CharField(default=datetime.today().strftime("%Y-%m-%d"),max_length=300)
class NewUsersLog(models.Model):
    created_week=models.CharField(default=week_num,max_length=200)
