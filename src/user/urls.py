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
from user.views.user_views import *
from user.views.role_user_views import *


app_name = 'user'
urlpatterns = [
    path('login/', userlogin, name='login'),
    path('logout/',userlogout, name='logout'),
    path('user/add', add_or_edit, name = 'add'),
    path('users', list, name = 'list'),
    path('user/<int:id>/update', add_or_edit, name = 'edit'),
    path('toggle_status/<int:id>/', user_status, name='status'),
    

    path('user/Add-role/',add_role,name="add_role"),
    path('user/List-role/',list_role,name="list_role"),
    path('user/<int:id>/edit-role',edit_role,name="edit_role"),
    path('user/<int:id>/delete-role',delete_role,name="delete_role"),
]
