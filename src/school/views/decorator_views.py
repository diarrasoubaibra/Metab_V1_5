from django.shortcuts import redirect
from django.urls import reverse
from requests import request
from school.models.app_setting_model import AppSettingsModel
from school.models.school_model import SchoolModel

def check_settings(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Vérifier si les paramètres de l'application et de l'école existent
        app_settings_exist = AppSettingsModel.objects.first()
        school_settings_exist = SchoolModel.objects.first()

        # L'utilisateur n'a pas encore ajouté les paramètres de l'application, rediriger vers l'ajout d'AppSettings
        if not app_settings_exist and request.path != reverse('school:add_setting'):
            return redirect('school:add_setting')

        # L'utilisateur a ajouté AppSettings mais pas encore SchoolSettings, rediriger vers l'ajout de SchoolSettings
        if app_settings_exist and not school_settings_exist and request.path != reverse('school:add'):
            return redirect('school:add')

        # L'utilisateur ne peut plus accéder à ces pages une fois les deux paramètres ajoutés
        if app_settings_exist and school_settings_exist:
            excluded_paths = [reverse('school:add_setting'), reverse('school:add')]
            if request.path in excluded_paths:
                return redirect('dashboard:dashboard')  # Rediriger vers le tableau de bord ou autre page une fois tout configuré

        # Si tout est en ordre, exécuter la vue
        return view_func(request, *args, **kwargs)

    return wrapper_func
