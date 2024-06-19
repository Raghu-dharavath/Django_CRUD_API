#################  APIView  ###################

""" 

from django.shortcuts import render
from django.http import request
from rest_framework.views import APIView
from rest_framework.response import Response        
from .models import Student

# Create your views here.
class StudentDetails(APIView):
    def get(self, request):
        s_details = Student.objects.all().values()
        return Response({'Message':'Student details list', 'details':s_details})
    
    def post(self, request):
        Student.objects.create(id=request.data["id"],
                               name = request.data["name"],
                               branch = request.data["branch"],
                               age = request.data["age"],
                               city = request.data["city"])
        student = Student.objects.all().filter(id=request.data["id"]).values()
        return Response({'Message':'New Student added', 'details':student})

 """

#################  ModelViewSet  ###############

from django.http import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from .models import Student, Employee, Mobile
from .serializers import EmployeeSerializer, StudentSerializer, MobileSerializer


class StudentDetails(APIView):
    serializer_class = StudentSerializer
    def get(self, request):
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if(serializer.is_valid):
            Student.objects.all(id=serializer.data.get("id"),
                                 name=serializer.data.get("name"),
                                 salary = serializer.data.get("salary")
                                )
        student = Student.objects.all().filter(id=request.data['id']).values()
        return Response({'Message':'New Employee added!','New_emplyee':student})
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer