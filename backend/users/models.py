from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone


class MyUserManager(BaseUserManager):
    def create_user(self, username, password, role,**extra_fields):
        user = self.model(
            username=username
        )
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        
        user.role=role
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, role,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, role, **extra_fields)    

class NewUser(AbstractBaseUser):
    objects = MyUserManager()
    class Meta:
        # managed = False
        db_table = 'user_entity'

    username = models.CharField(db_column='username', unique=True, max_length=20)
    role = models.CharField(db_column='userRole', unique=True, max_length=20)
    password = models.CharField(db_column='userPassword', max_length=256)
   
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.user_id) + " (%s)" % str(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    objects = MyUserManager()
    class Meta:
        # managed = False
        db_table = 'user_entity'

    username = models.CharField(db_column='username', unique=True, max_length=20)
    password = models.CharField(db_column='userPassword', max_length=256)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.user_id) + " (%s)" % str(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True