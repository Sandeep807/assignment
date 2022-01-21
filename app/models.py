
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .managers import *

class SignUp(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    email_verify=models.BooleanField(default=False)
    otp=models.IntegerField(null=True,blank=True)
    profile_pic=models.ImageField(upload_to='image/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserManager()

