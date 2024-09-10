from django.shortcuts import render, redirect
from student.models.absence_model import AbsenceModel
from student.forms.absence_form import AbsenceFoms
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings


@login_required(login_url='user:login')
@check_settings
def add_abs(request):
    context={"title":"Ajout Absence"}

    if request.method == "POST":
        print(request.POST)
        formA =AbsenceFoms(request.POST)
        context["formA"] = formA
        if formA.is_valid():
            print("form is valid")
            print(formA.cleaned_data)
            formA.save()
            return redirect('student:list_abs')
        else:
            return render(request,"student/absence.html")

    # context={'elev_form':elev_form}
    formA = AbsenceFoms()
    context["formA"] = formA

    return render(request,"student/absence.html",context)

@login_required(login_url='user:login')
def list_abs(request):
    absences = AbsenceModel.objects.all()
    absence_count = AbsenceModel.objects.count()

    context = {
        'absences':absences,
        'absence_count':absence_count
        
    }
    return render(request, "student/list_abs.html", context)


@login_required(login_url='user:login')
def update_abs(request,id):
    absence = AbsenceModel.objects.get(id=id)
    
    context={"title":"Modifier Absence"}

    if request.method == "POST":
        print(request.POST)
        formA =AbsenceFoms(request.POST, instance=absence)
        context["formA"] = formA
        if formA.is_valid():
            print("form is valid")
            print(formA.cleaned_data)
            formA.save()
            return redirect('student:list_abs')
        else:
            return render(request,"student/absence.html")

    # context={'elev_form':elev_form}
    formA = AbsenceFoms(instance=absence)
    context["formA"] = formA

    return render(request,"student/absence.html",context)
