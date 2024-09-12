from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api_views.student_views import student_view, student_detail
from .api_views.teacher_views import teacher_view, teacher_detail
from .api_views.user_views import user_detail, user_view

router = routers.DefaultRouter()
#router.register(r'students', student_view)

urlpatterns = [
   #path('', include(router.urls)), 
   path('student', student_view),
   path('student/<int:pk>', student_detail),

   path('teacher', teacher_view),
   path('teacher', teacher_detail),

   path('user', user_view),
   path('user/<int:pk>', user_detail)
]