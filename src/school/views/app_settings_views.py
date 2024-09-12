from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from school.forms.app_setting_form import AppSettingFoms
from school.models.app_setting_model import AppSettingsModel
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings


@login_required(login_url='user:login')
@check_settings
def sett_list(request):
    appsettings = AppSettingsModel.objects.all()
    ap_count = AppSettingsModel.objects.count()
    context = {
        'appsettings':appsettings,
        'ap_count':ap_count
        
    }
    return render(request, "settings_app/appsetting_list.html", context)


@login_required(login_url='user:login')
@check_settings
def setting_details(request, id):
    appsetting = AppSettingFoms.objects.get(id=id)
    context = {"appsetting":appsetting}
    return render(request, "settings_app/appsetting_detail.html", context)

@check_settings
def add_setting(request):
    context = {"title": "Ajout de setting"}
    app_settings_exist = AppSettingsModel.objects.first()

    if request.method == "POST":
        if app_settings_exist:
            return redirect('school:add')  # Rediriger vers le tableau de bord si les paramètres existent déjà

        appsetting_form = AppSettingFoms(request.POST)
        context["appsetting_form"] = appsetting_form
        if appsetting_form.is_valid():
            appsetting_form.save()
            return redirect('school:add')
        else:
            return render(request, "settings_app/appsetting_form.html", context)

    appsetting_form = AppSettingFoms()
    context["appsetting_form"] = appsetting_form

    return render(request, "settings_app/appsetting_form.html", context)


@login_required(login_url='user:login')
@check_settings
def edit_setting(request, id):
    appsetting = AppSettingsModel.objects.get(id=id)
 
    context = {
        "title":"Modifier le paramettre"
    }

    if request.method == "POST":
        appsetting_form = AppSettingFoms(request.POST, instance=appsetting)
        if appsetting_form.is_valid():
            appsetting_form.save()
            return redirect('school:sett_list')
        
    appsetting_form = AppSettingFoms(instance = appsetting)

    context["appsetting_form"] = appsetting_form

    return render(request,"settings_app/appsetting_form.html",context)


@login_required(login_url='user:login')
def delete_setting(request, id):
    appsetting = get_object_or_404(AppSettingsModel, id=id)
    if request.method == "POST":
        appsetting.delete()
        return redirect('school:sett_list')
    context = {"appsetting": appsetting, "title": "Supprimer Ecole"}
    return render(request, "settings_app/appsetting_confirm_delete.html", context)

from django.shortcuts import redirect
from school.models import SchoolModel, AppSettingsModel


