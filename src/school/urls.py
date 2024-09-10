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
from school.views.school_views import *
from school.views.app_settings_views import *


app_name="school"
urlpatterns = [
    path('school',list,name="list"),
    path('school/add/',add,name="add"),
    path('school/update/<int:id>',edit,name="edit"),
    # path('delete/<int:id>',edit,name="delete"),
    path('school/details/<int:id>',edit,name="details"),

    path('appsetting',sett_list,name="sett_list"),
    path('add_setting/',add_setting,name="add_setting"),
    path('edit_setting/<int:id>',edit_setting,name="edit_setting"),
    path('delete_setting/<int:id>',delete_setting,name="delete_setting"),
    path('setting_details/<int:id>',setting_details,name="setting_details"),

]
