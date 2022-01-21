from django.contrib.auth.base_user import BaseUserManager
from .email import *
import random
class UserManager(BaseUserManager):
    use_in_migrations=True

    def create(self,email,password=None,**extra_fields):
        if email:
            email=self.normalize_email(email)
            user=self.model(email=email,**extra_fields)
            user.set_password(password)
            user.otp=random.randint(1000,9999)
            user.save(using=self._db)
            send_otp(email,user.first_name,user.otp)
            return user
        else:
            raise ValueError('Email id is required')
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff is true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser is true') 

        return self.create(email,password,**extra_fields)


