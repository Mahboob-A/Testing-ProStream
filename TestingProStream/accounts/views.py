from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.conf import settings
from .models import CustomUser
from .serializer import CustomUserAllFieldsSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



class RegisterAPI(APIView): 
        def post(self, request, format=None): 
                serializer = CustomUserAllFieldsSerializer(data=request.data)
                print('serializer: ', serializer)
                print('request.data 1: ', request.data)
                if serializer.is_valid(): 
                        print('self.validated_data: ', serializer.validated_data)
                        print('request.data 2: ', request.data)
                        username = serializer.validated_data.get('username')
                        email = serializer.validated_data.get('email')
                        print('username: ', username)
                        print('email: ', email)
                        # user = CustomUser.objects.create_user(**serializer.validated_data)
                        serializer.save()
                        print('serializer.data: ', serializer.data)
                        return Response({'status' : 'success', 'data' : 'user created successfully !!'}, status=status.HTTP_200_OK)
                return Response({'status' : 'error', 'data' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class RegisterAPI2(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserAllFieldsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)