from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api_views.student_views import student_view

router = routers.DefaultRouter()
#router.register(r'students', student_view)

urlpatterns = [
   #path('', include(router.urls)), 
   path('', student_view),
]