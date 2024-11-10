from django.shortcuts import render,redirect,get_object_or_404
from .models import Mobile
from .serializers import MobileSerializers
from .forms import MobileForm
from django.http import HttpResponse
from rest_framework import viewsets


""" class ApiView(viewsets.ModelViewSet):
    serializer_class = MobileSerializers
    queryset = Mobile.objects.all() """

def mobileform(request):  # Changed the function name to lowercase
    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mobiles_list")
    else:
        form = MobileForm()
    return render(request, "createform.html", {'form': form})


def get_data(request):
    data = Mobile.objects.all()
    return render(request, 'mobile_list.html', {"mobile_data":data})

def edit_data(request, id):
    data = Mobile.objects.get(id=id)
    return render(request, 'update.html', {"data":data})

def update_data(request, id):
    data = Mobile.objects.get(id=id)
    if request.method=="POST":
        form = MobileForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('mobiles_list')
    else:
        form = MobileForm(instance=data)
        
    return render(request, 'update.html',{'form':form,'mobile_data':data})

def delete_mobile(request, id):
    data = Mobile.objects.get(id=id)
    data.delete()
    
    return redirect('mobiles_list')
