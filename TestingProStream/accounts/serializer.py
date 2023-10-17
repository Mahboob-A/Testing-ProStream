

from rest_framework import serializers 

from .models import CustomUser 

class CustomUserAllFieldsSerializer(serializers.ModelSerializer): 
        extra_fields = {'password' : {'write_only' : True}}
        class Meta: 
                model = CustomUser 
                fields = '__all__'