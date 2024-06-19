from rest_framework import serializers
from .models import Employee, Mobile

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="enter student id")
    name = serializers.CharField(label="enter sname")
    branch = serializers.CharField(label="enter sbranch")
    age = serializers.IntegerField(label ="enter age")
    city = serializers.CharField(label="enter scity")

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'