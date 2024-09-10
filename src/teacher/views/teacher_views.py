from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from teacher.forms.teacher_forms import TeacherFoms
from teacher.models.teacher_model import TeacherModel
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings



# Create your views here.
@login_required(login_url='user:login')
@check_settings
def list(request):
    query = request.GET.get('q')
    if query:
        teachers = TeacherModel.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
    else:
        teachers = TeacherModel.objects.all()

    teacher_count = teachers.count()
    context = {
        'teachers': teachers,
        'teacher_count': teacher_count,
        'query': query,
    }
    return render(request, "teacher/teacher_list.html", context)

@login_required(login_url='user:login')
@check_settings
def add(request):
    context={"title":"Ajouter un eleve"}

    if request.method == "POST":
        print(request.POST)
        form = TeacherFoms(request.POST)
        context["form"] = form
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('teacher:list')
        else:
            return render(request,"teacher/teacher_form.html")
    
    # context={'teach_form': teach_form}
    form = TeacherFoms()
    context["form"] = form

    return render(request,"teacher/teacher_form.html",context)

@login_required(login_url='user:login')
@check_settings
def edit(request, id):
    teacher = TeacherModel.objects.get(id=id)

    context = {"title":"Modifier professeur"}

    if request.method == "POST":
        form = TeacherFoms(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher:list')
        
    form = TeacherFoms(instance = teacher)

    context["form"] = form
    
    return render(request,"teacher/teacher_form.html",context)


@login_required(login_url='user:login')
@check_settings
def delete(request, id):
    teacher = TeacherModel.objects.get(id = id)
    teacher.delete()
    return redirect('teacher:list')
