from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from school.forms.school_form import SchoolFoms
from school.models.school_model import SchoolModel
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings


@login_required(login_url='user:login')
@check_settings
def list(request):
    schools = SchoolModel.objects.all()
    school_count = SchoolModel.objects.count()
    context = {
        'schools':schools,
        'school_count':school_count
        
    }
    return render(request, "school/school_list.html", context)


@login_required(login_url='user:login')
@check_settings
def details(request, id):
    school = SchoolModel.objects.get(id=id)
    context = {"school":school}
    return render(request, "school/school_detail.html", context)

@check_settings
def add(request):
    context={"title":"Ajouter Ecole"}
    school_settings_exist = SchoolModel.objects.first()
    if request.method == "POST":
        if school_settings_exist:
            return redirect('user:login')
        
        school_form =SchoolFoms(request.POST)
        context["school_form"] = school_form
        if school_form.is_valid():
            print("form is valid")
            print(school_form.cleaned_data)
            school_form.save()
            return redirect('user:login')
        else:
            return render(request,"school/school_form.html")

    # context={'elev_form':elev_form}
    school_form = SchoolFoms()
    context["school_form"] = school_form

    return render(request,"school/school_form.html",context)


@login_required(login_url='user:login')
@check_settings
def edit(request, id):
    school = SchoolModel.objects.get(id=id)
    context = {"title": "Modifier l'école"}

    if request.method == "POST":
        school_form = SchoolFoms(request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            return redirect('school:list')
    else:
        school_form = SchoolFoms(instance=school)

    context["school_form"] = school_form

    return render(request, "school/school_form.html", context)


@login_required(login_url='user:login')
@check_settings
def delete(request, id):
    school = get_object_or_404(SchoolModel, id=id)
    if request.method == "POST":
        school.delete()
        return redirect('school:list')
    context = {"school": school, "title": "Supprimer Ecole"}
    return render(request, "school/school_confirm_delete.html", context)
