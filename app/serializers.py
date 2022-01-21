from dataclasses import field
import email
from pyexpat import model
from rest_framework import serializers
from .models import *

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=SignUp
        fields=('first_name','last_name','email','password','profile_pic')

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()