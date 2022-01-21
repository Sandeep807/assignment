import email
from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,logout,login
# Create your views here.


class SignUpView(APIView):
    def post(self,request):
        try:
            serializer=SignUpSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request):
        try:
            data=request.data
            obj=SignUp.objects.filter(email=data['email']).first()
            if obj:
                serializer=SignUpSerializer(obj,data,partial=True,context={'request':request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({'message':'Email id not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class VerifyOtp(APIView):
    def post(self,request):
        try:
            data=request.data
            user=SignUp.objects.filter(email=data['email']).first()
            if user:
                if user.otp==int(data['otp']):
                    user.email_verify=True
                    user.save()
                    return Response({'message':'Email verified successful'},status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Otp not match'},status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({'message':'Email id not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self,request):
        try:
            data=request.data
            obj=SignUp.objects.filter(email=data['email']).first()
            if obj:
                serializer=LoginSerializer(data=data)
                if serializer.is_valid():
                    user=authenticate(email=serializer.data['email'],password=serializer.data['password'])
                    if user:
                        return Response({'message':'Login successful'},status=status.HTTP_200_OK)
                    else:
                        return Response({'message':'Invalid email and password'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({'message':'Email not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class LogOut(APIView):
    def post(self,request):
        try:
            logout(request)
            return Response({'message':'Logout successful'})
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)