from django.shortcuts import redirect
from django.urls import reverse
from school.models.app_setting_model import AppSettingsModel
from school.models.school_model import SchoolModel

def check_settings(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Vérifier si les paramètres de l'application et de l'école existent
        app_settings_exist = AppSettingsModel.objects.exists()
        school_settings_exist = SchoolModel.objects.exists()

        # Exclure les vues de paramétrage de la vérification
        excluded_paths = [reverse('school:add_setting'), reverse('school:add')]

        if request.path in excluded_paths:
            return view_func(request, *args, **kwargs)

        # Si les paramètres ne sont pas encore configurés
        if not app_settings_exist:
            return redirect('school:add_setting')  # Rediriger vers la page de configuration de l'application
        if not school_settings_exist:
            return redirect('school:add')  # Rediriger vers la page de configuration de l'école

        # Si tout est en ordre, exécuter la vue
        return view_func(request, *args, **kwargs)
    
    return wrapper_func
