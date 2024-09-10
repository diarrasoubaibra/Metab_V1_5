from django.shortcuts import render, redirect
from student.forms.student_cards_form import StudentCardFoms
from student.models.student_cards_model import StudentCardsModel
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings


@login_required(login_url='user:login')
@check_settings
def add_card(request):
    context={"title":"Carte Etudiant"}

    if request.method == "POST":
        print(request.POST)
        formS =StudentCardFoms(request.POST)
        context["formS"] = formS
        if formS.is_valid():
            print("form is valid")
            print(formS.cleaned_data)
            formS.save()
            return redirect('student:list_card')
        else:
            return render(request,"student/student_cards.html")


    formS = StudentCardFoms()
    context["formS"] = formS

    return render(request,"student/student_cards.html",context)


@login_required(login_url='user:login')
@check_settings
def list_card(request):
    studentCardss = StudentCardsModel.objects.all()
    carte_count = StudentCardsModel.objects.count()
    context = {
        'studentCardss':studentCardss,
        'carte_count':carte_count
        
    }
    return render(request, "student/list_card.html", context)
