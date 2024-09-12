from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from school.models.app_setting_model import AppSettingsModel
from school.models.school_model import SchoolModel
from user.models.user_model import UserModel
from user.forms.user_form import UserFoms
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings



# Create your views here.
@login_required(login_url='user:login')
@check_settings
def list(request):
    query = request.GET.get('q')  # On récupère la valeur de la recherche
    if query:
        users = UserModel.objects.filter(
            Q(pseudo__icontains=query)  # Recherche par pseudo
              # Recherche par email (ou autre champ pertinent)
        )
    else:
        users = UserModel.objects.all()  # Si pas de recherche, afficher tous les utilisateurs
    
    user_count = users.count()
    context = {
        'users': users,
        'user_count': user_count,
        'query': query,  # Envoyer la requête de recherche pour la garder dans le template
    }
    return render(request, "user/user_list.html", context)


@login_required(login_url='user:login')
@check_settings
def add_or_edit(request, id=None):
    if id:
        user = get_object_or_404(UserModel, id=id)
        context = {"title": "Modifier Utilisateur"}
    else:
        user = None
        context = {"title": "Ajouter Utilisateur"}

    if request.method == "POST":
        form = UserFoms(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)

            if not user.pk or form.cleaned_data.get('password'):
                user.set_password(form.cleaned_data['password'])
                print(user.password)  # Vérifiez que le mot de passe est haché

            user.save()
            return redirect('user:list')
    else:
        form = UserFoms(instance=user)

    context["form"] = form
    return render(request, "user/user_form.html", context)

@check_settings
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')

    if request.method == 'POST':
        pseudo = request.POST['pseudo']
        password = request.POST['password']
        
        user = authenticate(request, username=pseudo, password=password)
        if user is not None:
            login(request, user)

            # Vérifier si l'utilisateur est un super utilisateur
            if user.is_superuser:
                # Vérifier si l'application ou l'école n'est pas encore configurée
                if not SchoolModel.objects.exists():
                    return redirect('school/add_setting/')
                elif SchoolModel.objects.exists():
                    return redirect('dashboard:dashboard')

                if not AppSettingsModel.objects.exists():
                    return redirect('school/add/')  # Redirige vers la page de paramétrage
                elif SchoolModel.objects.exists():
                    return redirect('dashboard:dashboard')
            return redirect('dashboard:dashboard')  # Redirige vers le tableau de bord pour les utilisateurs normaux
        else:
            return render(request, 'user/login.html', {'error': 'Identifiant ou mot de passe incorrect.'})

    return render(request, 'user/login.html')




#Authentication

@login_required(login_url='user:login')
def userlogout(request):
    logout(request)
    return redirect(reverse('user:login'))

@login_required(login_url='user:login')
def user_status(request, id):
    user = get_object_or_404(UserModel, id=id)
    user.is_active = not user.is_active
    user.save()
    return redirect('user:list')

