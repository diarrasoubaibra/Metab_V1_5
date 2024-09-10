from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from student.forms.student_form import StudentFoms
from student.models.student_model import StudentModel
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings


@login_required(login_url='user:login')
@check_settings
def list(request):
    query = request.GET.get('q')
    if query:
        students = StudentModel.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(matricule__icontains=query)
        )
    else:
        students = StudentModel.objects.all()

    student_count = students.count()
    context = {
        'students': students,
        'student_count': student_count,
        'query': query,
    }
    return render(request, "student/student_list.html", context)


@login_required(login_url='user:login')
@check_settings
def add(request):
    context={"title":"Ajouter Eleve"}

    if request.method == "POST":
        print(request.POST)
        student_form =StudentFoms(request.POST)
        context["student_form"] = student_form
        if student_form.is_valid():
            print("student_form is valid")
            print(student_form.cleaned_data)
            student_form.save()
            return redirect('student:list')
        else:
            return render(request,"student/student_form.html")

    student_form = StudentFoms()
    context["student_form"] = student_form

    return render(request,"student/student_form.html",context)


@login_required(login_url='user:login')
@check_settings
def edit(request, id ):
    student = StudentModel.objects.get(id=id)
    context = {"title":"Modifier eleve"}
    if request.method == "POST":
        student_form = StudentFoms(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('student:list')
        
    form = StudentFoms(instance = student)

    context["student_form"] = student_form

    return render(request,"student/student_form.html",context)

@login_required(login_url='user:login')
def delete(request ,id):
    student = StudentModel.objects.get(id = id)
    student.delete()
    return redirect('student:list')
