from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from user.forms.role_user_form import RoleUserFoms
from user.models.role_user_model import RoleUserModel
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings



# Create your views here.
@login_required(login_url='user:login')
@check_settings
def list_role(request):
    roles = RoleUserModel.objects.all()
    role_count = RoleUserModel.objects.count()
    context = {
        'roles':roles,
        'role_count':role_count
        
    }
    return render(request, "user/roleuser_list.html", context)


@login_required(login_url='user:login')
@check_settings
def add_role(request):

    context={"title":"Ajout Role"}

    if request.method == "POST":
        print(request.POST)
        form1 =RoleUserFoms(request.POST)
        context["form1"] = form1
        if form1.is_valid():
            form1.save()
            return redirect('user:list_role')
        else:
            return render(request,"user/roleuser_form.html")

    form1 = RoleUserFoms()
    context["form1"] = form1

    return render(request,"user/roleuser_form.html",context)

@login_required(login_url='user:login')
@check_settings
def edit_role(request, id):
    role = get_object_or_404(RoleUserModel, id=id)
    context = {"title": "Modifier Role"}

    if request.method == "POST":
        form1 = RoleUserFoms(request.POST, instance=role)
        context["form1"] = form1
        if form1.is_valid():
            form1.save()
            return redirect('user:list_role')
        else:
            return render(request, "user/roleuser_form.html", context)

    form1 = RoleUserFoms(instance=role)
    context["form1"] = form1

    return render(request, "user/roleuser_form.html", context)

@login_required(login_url='user:login')
@check_settings
def delete_role(request, id):
    role = get_object_or_404(RoleUserModel, id=id)
    context = {"title": "Supprimer Role", "role": role}

    if request.method == "POST":
        role.delete()
        return redirect('user:list_role')
    return render(request, "user/roleuser_confirm_delete.html", context)