"""
URL configuration for webpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from Website import views
from crud import views
from django.urls import path
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', views.EmployeeViewSet)
router.register('mobile', views.MobileViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.Message, name='Message'),
    # path('Add', views.Add, name='Add'),
    path('Student/', views.StudentDetails.as_view()),
    path("",include(router.urls)),
    path("",include(router.urls))
]
