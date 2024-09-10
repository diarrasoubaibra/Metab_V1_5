from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings
from base.forms import AdressFoms
from base.models.address_model import AddressModel

# Create your views here.
@login_required(login_url='user:login')
@check_settings
def add(request):
    context={"title":"Ajouter Adress"}

    if request.method == "POST":
        print(request.POST)
        form =AdressFoms(request.POST)
        context["form"] = form
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('student:list')
        else:
            return render(request,"base/adress_form.html")

    # context={'elev_form':elev_form}
    form = AdressFoms()
    context["form"] = form

    return render(request,"base/address_form.html",context)


@login_required(login_url='user:login')
@check_settings
def list(request):
    address = AddressModel.objects.all()
    context = {
        'address': address,
        }
    
    return render(request, "base/address_list.html", context)


@login_required(login_url='user:login')
@check_settings
def edit(request, id):
    teacher = AddressModel.objects.get(id=id)

    context = {"title":"Modifier adresse"}

    if request.method == "POST":
        form = AdressFoms(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('address:list')
        
    address_form = AdressFoms(instance = teacher)

    context["form"] = address_form
    
    return render(request,"base/address_form.html",context)

@login_required(login_url='user:login')
@check_settings
def delete(request, id):
    address = AddressModel.objects.get(id = id)
    address.delete()
    return redirect('address:list')
