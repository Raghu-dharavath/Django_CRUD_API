from django.shortcuts import render
from django.http import HttpResponse
from django.http import request

# Create your views here.
def Message(request):
    return render(request, 'home.html', {'name':'Raghu'})
    
def Add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    sum = val1+val2
    return render(request, 'result.html',{'result':sum})