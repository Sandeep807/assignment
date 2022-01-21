from django.urls import path
from .views import *
urlpatterns=[
    path('sign_up/',SignUpView.as_view()),
    path('verify_otp/',VerifyOtp.as_view()),
    path('login/',Login.as_view()),
    path('logout/',LogOut.as_view()),


]