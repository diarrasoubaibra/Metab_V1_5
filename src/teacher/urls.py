"""
URL configuration for monetabv1_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from teacher.views.teacher_views import *


app_name="teacher"
urlpatterns = [
    path('', list,name="list"),
    path('add',add,name="add"),
    path('update/<int:id>',edit,name="edit"),
    path('delete/<int:id>',delete,name="delete"),
]
