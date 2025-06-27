from rest_framework import serializers
from .models import HostelFeeItem, HostelItem, StudentItem, Room
from django.contrib.auth.models import User

class HostelFeeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelFeeItem
        fields = '__all__'
        
        
class HostelItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelItem
        fields = '__all__'
        

class StudentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentItem
        fields = '__all__'
        

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'        
        

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)   
    
    class Meta:
        model = User
        fields=['username', 'password', 'email']
        
    def create(self, validated_data):
        user= User.objects.create_user(username=validated_data['username'], password=validated_data['password'],email=validated_data.get('email', ''))
        return user