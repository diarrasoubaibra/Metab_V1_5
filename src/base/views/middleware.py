from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
from school.models import SchoolModel, AppSettingsModel
from django.contrib.auth.decorators import login_required

# @login_required(login_url='user:login')
class EnsureSettingsMiddleware:
    pass
    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def __call__(self, request):
    #     # Les URL à ignorer pour éviter la boucle de redirection
    #     excluded_paths = [
    #         reverse('user:login'),        # URL de la page de connexion
    #         reverse('user:logout'),       # URL de la page de déconnexion
    #         '/school/add/',          # URL pour ajouter une école
    #         '/school/add_setting/',  # URL pour ajouter les paramètres de l'application
    #         '/admin/',               # URL pour accéder à l'admin Django
    #     ]

    #     # Vérifier si l'utilisateur est connecté
    #     if request.user.is_authenticated:
    #         # Si l'utilisateur est un superuser, on peut lui permettre d'accéder
    #         # if request.user.is_superuser:
    #         #     return self.get_response(request)

    #         # Si l'utilisateur tente d'accéder à une page non exclue
    #         if not any(request.path.startswith(path) for path in excluded_paths):
    #             # Vérifier si les paramètres de l'application et de l'école existent
    #             app_settings_exist = AppSettingsModel.objects.exists()
    #             school_settings_exist = SchoolModel.objects.exists()

    #             # Si les paramètres ne sont pas encore configurés
    #             if not app_settings_exist:
    #                 return redirect('/school/add_setting/')  # Rediriger vers l'ajout des paramètres
    #             if not school_settings_exist:
    #                 return redirect('/school/add/')  # Rediriger vers l'ajout de l'école

    #     # Si tout est correct ou l'utilisateur n'est pas connecté, on continue normalement
    #     response = self.get_response(request)
    #     return response
